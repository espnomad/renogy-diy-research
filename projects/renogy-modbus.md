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

| Repo | Short Description | Interesting for me |
|------|------------------|--------------------|
| [rosswarren/renogymodbus](https://github.com/rosswarren/renogymodbus) | Python scripts to read/write Renogy Modbus registers, includes example register maps for Rover MPPT controllers. | Register map decoding, Python examples I can port to ESPHome/Arduino. RJ45 Cable modbus Canbus pinout |
| [cyrils/renogy-bt](https://github.com/cyrils/renogy-bt) | bluetooth integration of the BT-2 working over modbus | great [documentation](https://github.com/cyrils/renogy-bt/discussions/94) |
| [sophienyaa/NodeRenogy](https://github.com/sophienyaa/NodeRenogy) | Node.js library for communicating with Renogy charge controllers via Modbus. | Useful to see JSON data structures and async patterns; could inspire HA integrations. |
| [wrybread/ESP32ArduinoRenogy](https://github.com/wrybread/ESP32ArduinoRenogy) | Arduino code for ESP32 to read Renogy Rover controllers over RS485. | Direct ESP32 implementation, good starting point for firmware. |
| [menloparkinnovation/renogy-rover](https://github.com/menloparkinnovation/renogy-rover) | Arduino sketches and docs for Renogy Rover Modbus integration. | Shows early decoding attempts and practical wiring examples. |
| [neilsheps/Renogy-BT2-Reader](https://github.com/neilsheps/Renogy-BT2-Reader) | Logs and decodes Renogy BT2 data stream, Python-based. | Useful to cross-reference BT2 vs. RS485 values and protocol framing. |
| [CircuitState RS-485 tutorial](https://www.circuitstate.com/tutorials/what-is-rs-485-how-to-use-max485-with-arduino-for-reliable-long-distance-serial-communication/) | General tutorial on RS-485 communication with Arduino using MAX485. | Hardware-level context for reliable long-distance comms; complements protocol decoding. |

--- 
