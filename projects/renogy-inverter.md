# Project: Renogy inverter

- **Link**: (add your primary reference link here)
- **Author**: Toon Nelissen
- **Type**: ESP32 / IO
- **Focus**: Remote on/off control + status LED read
- **Status**: (Active , last check: 2025-10)
- **Tags**: #inverter #esp32 #homeassistant #gpio

---

## 🔎 Summary
This board enables smart control of Renogy inverters using a signal relay and an I2C IO expander.  
It integrates the original RJ45 toggle switch controller and LED indicators (green/red).

---

## 🛠️ TODO

- [ ] Measure LED control voltage
- [ ] Measure RJ45 connector pinout and confirm layout

---

## 🧩 Functional Overview

The board includes **two female RJ45 connectors**:
- One connects to the **Renogy inverter**
- One connects to the **original Renogy controller** (toggle switch + dual LEDs)

### Board Responsibilities:
- ✅ Toggle inverter ON by shorting **Button Input ↔ VIN** (via signal relay)
- ✅ Read inverter **Green LED** status (via input)
- ✅ Read inverter **Red LED** status (via input)
- ✅ Detect **toggle switch** state of original controller (via input)
- ✅ Mirror **Green LED** to controller’s LED (pass-through)
- ✅ Mirror **Red LED** to controller’s LED (pass-through)
- 🔄 (Optional) Detect if inverter is powered by sensing **VIN**

---

## 🔌 I/O Overview (via I2C IO Expander)

| Type    | Signal               | Description                     |
|---------|----------------------|---------------------------------|
| Input   | VIN sense (optional) | Detect if inverter has power    |
| Input   | Red LED              | Fault LED signal from inverter  |
| Input   | Green LED            | ON LED signal from inverter     |
| Input   | Toggle switch        | Controller's toggle position    |
| Output  | Signal Relay         | Trigger inverter ON/OFF         |

---

## 💡 Extra Ideas

Consider using a **22mm dual-color illuminated momentary push button** as a standalone controller:

> GUUZI 12V-24V / 10A Waterproof Momentary Push Button  
> Illuminated Green/Red LED — Start Push Button with Plug Wire

This button could be wired to a **RJ45 plug** and directly interface with the board/controller.

---

## 💡 Useful Code / Config
```yaml
# Example (placeholder)
# switch:
#   - platform: gpio
#     pin: 21
#     name: "Inverter Power"
```

---

## 🗒️ Notes

- 1x WS2812 RGB LED for visual feedback (e.g. status, fault, control)
- This board **does not include busbar attachment points**
- Designed to work with the [ESPnomad base board](https://github.com/espnomad/renogy-diy-research) via I2C
  
---

## 📚 Sources

- [-RJ45 pinout](https://diysolarforum.com/threads/renogy-remote-switch-wiring-diagram.15308/post-1527985)

