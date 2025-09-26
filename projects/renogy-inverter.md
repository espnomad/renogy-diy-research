# Project: Renogy inverter

- **Link**: (add your primary reference link here)
- **Author**: Toon Nelissen
- **Type**: ESP32 / IO
- **Focus**: Remote on/off control + status LED read; potential UART/RS interface if supported
- **Status**: (Active , last check: 2025-09)
- **Tags**: #inverter #esp32 #homeassistant #gpio

---

## 🔎 Summary
Interface ideas for Renogy inverters: one-button panel replication, opto isolation, HA switch + status LEDs.

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
- Debounce and press length (short vs long)
- LED readout via voltage divider + ADC
- Safety considerations
  
---

## 📚 Sources
