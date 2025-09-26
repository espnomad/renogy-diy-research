import os, re, json, sys
from datetime import datetime, timezone
from dateutil import parser as dtparse
import requests
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
PROJECTS_DIR = ROOT / "projects"

INDEX_START = "<!--INDEX:START-->"
INDEX_END = "<!--INDEX:END-->"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# Simple project registry: filename -> (Type, Focus)
# If you want to keep these in front-matter later, adjust parsing here.
PROJECT_META = {
    "renogy-modbus.md":   ("Arduino / ESPHome", "RS485/Modbus decode for MPPT & DC-DC"),
    "renogy-bt-2.md":     ("ESP32 / RS485", "Reverse-engineering BT-2 adapter protocol"),
    "renogy-shunt.md":    ("ESPHome / INA2xx", "Battery shunt measurement + HA"),
    "renogy-inverter.md": ("ESP32 / IO", "Remote inverter on/off, status"),
}

REPO_URL_RE = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")

def find_repo_urls(md_text: str):
    """Return list of unique GitHub owner/repo tuples found in a markdown file."""
    seen = set()
    for m in REPO_URL_RE.finditer(md_text):
        owner, repo = m.group(1), m.group(2)
        seen.add((owner, repo))
    return sorted(seen)

def github_repo_pushed_at(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    r = requests.get(url, headers=HEADERS, timeout=20)
    if r.status_code != 200:
        return None
    data = r.json()
    # prefer pushed_at (most recent activity), fallback updated_at
    return data.get("pushed_at") or data.get("updated_at")

def most_recent_date(iso_dates):
    """Return most recent ISO date (YYYY-MM-DD) from a list of ISO timestamps."""
    latest = None
    for ts in iso_dates:
        try:
            dt = dtparse.isoparse(ts)
        except Exception:
            continue
        if latest is None or dt > latest:
            latest = dt
    if not latest:
        return "_TBD (auto)_"
    # Normalize to date in UTC
    return latest.astimezone(timezone.utc).date().isoformat()

def build_index_rows():
    rows = []
    for mdfile in sorted(PROJECTS_DIR.glob("*.md")):
        name = mdfile.stem.replace("-", " ").title()  # e.g., "Renogy Modbus"
        ptype, focus = PROJECT_META.get(mdfile.name, ("—", "—"))

        # parse sources for repo links
        text = mdfile.read_text(encoding="utf-8")
        repos = find_repo_urls(text)
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
    before = readme_text[:start + len(INDEX_START)]
    after = readme_text[end:]
    # Ensure a blank line after START, before END
    return before + "\n" + table_text + "\n" + after

def main():
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
