# Project: Renogy Shunt

- **Link**: (add your primary reference link here)
- **Author**: (name or org)
- **Type**: ESPHome / INA2xx
- **Focus**: Battery current/voltage/power readout (INA226/INA228), calibration, HA integration
- **Status**: (Active / Inactive, last check: YYYY-MM)
- **Tags**: #shunt #ina226 #ina228 #esphome #homeassistant

---

## 🔎 Summary
Notes on wiring (Kelvin), RC input filtering, scaling, temperature compensation, and HA sensors.

---

## 💡 Useful Code / Config
```yaml
# Example (placeholder)
# sensor:
#   - platform: ina228
#     address: 0x40
#     shunt_resistance: 0.0005
#     current:
#       name: "Battery Current"
```

## 🗒️ Notes
- Shielding/grounding for long runs
- Differential cap and series resistors near ADC

---

## 📚 Sources

---
