# 🔋 Renogy DIY Research & References

This repo collects **community projects, integrations, and experiments** with Renogy hardware (MPPT, DC-DC, shunts, inverters, …).  
It’s my **personal knowledge base** to track useful repos, code snippets, and documentation for future builds.

---

## 📑 Project Index

> The **Last Update** column is auto-filled by a GitHub Action that looks at the GitHub repos listed in each project page’s **Sources** section and uses the most recent `pushed_at` date.

<!--INDEX:START-->
| Project | Type | Focus | Last Update | Page |
|--------|------|-------|-------------|------|
| Renogy Inverter | ESP32 / IO | Remote inverter on/off, status | _TBD (auto)_ | [projects/renogy-inverter.md](projects/renogy-inverter.md) |
| Renogy Modbus | Arduino / ESPHome | RS485/Modbus decode for MPPT & DC-DC | _TBD (auto)_ | [projects/renogy-modbus.md](projects/renogy-modbus.md) |
| Renogy Shunt | ESPHome / INA2xx | Battery shunt measurement + HA | _TBD (auto)_ | [projects/renogy-shunt.md](projects/renogy-shunt.md) |
<!--INDEX:END-->

---

## 🧰 How I use this

- Each project gets its own page in `/projects/` using the template in `/templates/project-template.md`.
- Under **Sources**, list one or more GitHub repos (one per bullet).  
  The Action will read these links and update the README’s **Last Update** with the most recent commit date among them.

**Tags I use** (searchable):  
`#esphome`, `#arduino`, `#rs485`, `#modbus`, `#bt2`, `#shunt`, `#ina228`, `#inverter`.

---
