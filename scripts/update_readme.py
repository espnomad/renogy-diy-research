import os, re, sys
from datetime import timezone
from dateutil import parser as dtparse
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
PROJECTS_DIR = ROOT / "projects"

INDEX_START = "<!--INDEX:START-->"
INDEX_END = "<!--INDEX:END-->"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "renogy-diy-research-indexer/1.0",
}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# filename -> (Type, Focus)
PROJECT_META = {
    "renogy-modbus.md":   ("Arduino / ESPHome", "RS485/Modbus decode for MPPT & DC-DC"),
    "renogy-bt-2.md":     ("ESP32 / RS485", "Reverse-engineering BT-2 adapter protocol"),
    "renogy-shunt.md":    ("ESPHome / INA2xx", "Battery shunt measurement + HA"),
    "renogy-inverter.md": ("ESP32 / IO", "Remote inverter on/off, status"),
}

# Match GitHub repo links in ANY markdown context:
#  - plain URL: https://github.com/owner/repo
#  - markdown link: [text](https://github.com/owner/repo)
#  - with trailing slash, .git, query/anchors, or trailing punctuation
GITHUB_REPO_URL = re.compile(
    r"""https://github\.com/
        (?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)
        (?:\.git|/)?        # optional .git or trailing slash
        (?:[?#][^\s)\]]*)?  # optional query/hash
        """,
    re.VERBOSE | re.IGNORECASE,
)

def find_repo_urls(md_text: str):
    """Return unique (owner, repo) pairs found anywhere in a markdown string."""
    seen = set()
    for m in GITHUB_REPO_URL.finditer(md_text):
        owner = m.group("owner")
        repo = m.group("repo")
        # normalize casing as GitHub is case-insensitive for owner/repo
        key = (owner.strip(), repo.strip())
        seen.add(key)
    return sorted(seen)

def github_repo_pushed_at(owner: str, repo: str):
    """Return ISO timestamp of last activity for a repo, or None on failure."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=25, allow_redirects=True)
    except requests.RequestException as e:
        print(f"[WARN] Request error for {owner}/{repo}: {e}", file=sys.stderr)
        return None

    if r.status_code == 404:
        print(f"[WARN] Not found: {owner}/{repo}", file=sys.stderr)
        return None
    if r.status_code == 403 and "rate limit" in r.text.lower():
        print(f"[WARN] Rate limited by GitHub API; consider PAT in secrets.GITHUB_TOKEN", file=sys.stderr)
        return None
    if r.status_code != 200:
        print(f"[WARN] Unexpected {r.status_code} for {owner}/{repo}: {r.text[:120]}", file=sys.stderr)
        return None

    data = r.json()
    # prefer pushed_at (most recent commit activity), then updated_at
    return data.get("pushed_at") or data.get("updated_at")

def most_recent_date(iso_timestamps):
    """Return YYYY-MM-DD for latest timestamp in list, else '_TBD (auto)_'."""
    latest = None
    for ts in iso_timestamps:
        try:
            dt = dtparse.isoparse(ts)
        except Exception:
            continue
        if (latest is None) or (dt > latest):
            latest = dt
    if not latest:
        return "_TBD (auto)_"
    return latest.astimezone(timezone.utc).date().isoformat()

def build_index_rows():
    rows = []
    for mdfile in sorted(PROJECTS_DIR.glob("*.md")):
        name = mdfile.stem.replace("-", " ").title()
        ptype, focus = PROJECT_META.get(mdfile.name, ("—", "—"))

        text = mdfile.read_text(encoding="utf-8")
        repos = find_repo_urls(text)

        if not repos:
            last_update = "_TBD (auto)_"
        else:
            iso_dates = []
            for owner, repo in repos:
                ts = github_repo_pushed_at(owner, repo)
                if ts:
                    iso_dates.append(ts)
            last_update = most_recent_date(iso_dates)

        page_link = f"projects/{mdfile.name}"
        rows.append((name, ptype, focus, last_update, page_link))
    return rows

def render_table(rows):
    header = "| Project | Type | Focus | Last Update | Page |\n|--------|------|-------|-------------|------|"
    lines = [header]
    for name, ptype, focus, last_update, page in rows:
        lines.append(f"| {name} | {ptype} | {focus} | {last_update} | [{page}]({page}) |")
    return "\n".join(lines)

def replace_index_table(readme_text, table_text):
    start = readme_text.find(INDEX_START)
    end = readme_text.find(INDEX_END)
    if start == -1 or end == -1 or end < start:
        print("ERROR: INDEX markers not found or malformed in README.md", file=sys.stderr)
        sys.exit(1)
    before = readme_text[: start + len(INDEX_START)]
    after = readme_text[end:]
    return before + "\n" + table_text + "\n" + after

def main():
    if not README.exists():
        print("ERROR: README.md not found", file=sys.stderr)
        sys.exit(1)
    if not PROJECTS_DIR.exists():
        print("ERROR: projects/ directory not found", file=sys.stderr)
        sys.exit(1)

    rows = build_index_rows()
    new_table = render_table(rows)

    text = README.read_text(encoding="utf-8")
    updated = replace_index_table(text, new_table)

    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print("README.md updated.")
    else:
        print("README.md unchanged.")

if __name__ == "__main__":
    main()
