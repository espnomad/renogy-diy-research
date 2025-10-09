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

## 🧩 Functional Overview

The board includes **two female RJ45 connectors**:
- One connects to the **Renogy inverter**
- One connects to the **original Renogy controller** (toggle switch + dual LEDs)
And one screw terminal for a 12/24V pushbutton with red/green led

### Board Responsibilities:
- ✅ Toggle inverter ON by shorting **Button Input ↔ VIN** (via signal relay)
- ✅ Read inverter **Green LED** status (via input)
- ✅ Read inverter **Red LED** status (via input)
- ✅ Detect **toggle switch** state of original controller (via input)
- ✅ Mirror **Green LED** to controller’s LED (pass-through)
- ✅ Mirror **Red LED** to controller’s LED (pass-through)
- ✅ Detect if inverter is powered by sensing if **VIN** has power

---

## 🔌 I/O Overview (via 8ch MCP23008 I2C IO Expander)

| MCP Pin | Type    | Signal               | Description                     |
|---------|---------|----------------------|---------------------------------|
|GPO      | Input   | VIN sense (optional) | Detect if inverter has power    |
|GP1      | Input   | Red LED              | Fault LED signal from inverter  |
|GP2      | Input   | Green LED            | ON LED signal from inverter     |
|GP3      | Input   | Toggle switch        | Controller's toggle position    |
|GP4      | Input   | Push button          | push button                     |
|GP5      | Output  | Signal Relay         | Trigger inverter ON/OFF         |
|GP6      | Output  | 12V led green        | show on signal to push button   |
|GP7      | Output  | 12V led red          | show fault signal on push button|

For the Red and Green LED use a voltage divider 
```
5V from led ---[47k]---+---[100k]--- GND
                       |
                       +----> MCP input
```

For the VIN sense use a Divider + Zener Clamp
```
12V ---[82k]---+---- MCP input
               |
             [3.6V Zener]
               |
              GND
```

For to the toggle switch and push button use 
```
3.3V ---[10k]-+- MCP input
              |
            Button
              |
             GND
```

For controlling the 12V led's from the push button
```                                 
                              ^ +12V                  
                              |                       
                            +---+                     
                            | | |                     
                        LED | v |                     
                            |---|                     
                            +---+                     
                              |                       
            +---------+       |                       
 MCP out ---|  R1.2K  |------ 2n2222                  
            +---------+       v                       
                              |                       
                             ---GND                   
                              -                        
```

For controlling the 5v relay
```
                              ^ 5V                   
                               |                      
                           |------|                   
                           |      |                   
                         +---+  +------+              
                         |---|  |Relay |              
                   1n4002| ^ |  |Coil  |              
                         | | |  |      |              
                         +---+  +------+              
                           |      |                   
                           --------                   
                              |                       
            +---------+       |                       
 MCP out ---|  R1.2K  |------ 2n2222                  
            +---------+       v                       
                              |                       
                             ---GND                   
                              -            
```


---

## 🧰 RJ45 Pinout (Renogy Inverter & Controller)

| Pin | Signal         | Description                                       |
|-----|----------------|---------------------------------------------------|
| 1   | –              | Not connected                                     |
| 2   | GND            | Ground                                            |
| 3   | Button Input   | Signal wire to start the inverter (via relay)     |
| 4   | Green LED      | 5V signal line (inverter ON)                      |
| 5   | VIN            | Battery voltage (typically 12V)                   |
| 6   | –              | Not connected                                     |
| 7   | Red LED        | 5V signal line (fault indication)                 |
| 8   | –              | Not connected                                     |

---

## 💡 Extra Ideas

Consider using a **22mm dual-color illuminated momentary push button** as a standalone controller:

> GUUZI 12V-24V / 10A Waterproof Momentary Push Button  
> Illuminated Green/Red LED — Start Push Button with Plug Wire

---

## 💡 Useful Code / Config


---

## 🗒️ Notes

- 1x WS2812 RGB LED for visual feedback (e.g. status, fault, control)
- This board **does not include busbar attachment points**
- Designed to work with the [ESPnomad base board](https://github.com/espnomad/renogy-diy-research) via I2C
  
---

## 📚 Sources

- [-RJ45 pinout](https://diysolarforum.com/threads/renogy-remote-switch-wiring-diagram.15308/post-1527985)

