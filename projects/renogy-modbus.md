# Project: Renogy Modbus

- **Link**: (add your primary reference link here)
- **Author**: Toon Nelissen
- **Type**: Arduino / ESPHome
- **Focus**: RS485/Modbus decoding for Renogy MPPT & DC-DC (register maps, scaling, HA sensors)
- **Status**: (Active, last check: 2025-09)
- **Tags**: #rs485 #modbus #mppt #dc-dc #esphome #arduino

---

## 🔎 Summary
Short description of what this effort covers: Modbus frame format, register maps, decoding strategy, pitfalls (byte order, signedness), and links to code/examples.

---

## 💡 Useful Code / Config

```yaml
# Example (placeholder)
# sensor:
#   - platform: modbus_controller
#     address: 0x0100
#     name: "Battery SOC"
```

---

## 🗒️ Notes
- Register quirks or vendor differences
- Cable/termination notes (RS485 A/B, 120Ω)
- HA entity naming conventions

---

## 📚 Sources

--- 
