# Gridfinity Autopilot

## Description
An autonomous robot designed to move Gridfinity boxes on a 42x42 mm grid.  
The robot features a differential drive, a Z-lift mechanism, and a gripper with pressure arms.

## Hardware
| Component                | Quantity | Notes                        |
|--------------------------|---------:|------------------------------|
| [NEMA17 Stepper](https://www.omc-stepperonline.com/de/nema-17-bipolar-1-8deg-40ncm-0-4a-12v-42x42x39mm-4-draehte-17hs15-0404s)           | 4        | 40 Ncm 1.8°                  |
| [A4988 Driver](https://www.amazon.de/AZDelivery-Schritt-komplett-Stiftleisten-Kühlkörper/dp/B07C2V9GWC)             | 4        | Stepper driver               |
| [Endstop Switches](https://www.amazon.de/JZK-Mikroschalter-Mikro-Endschalter-Scharnierhebelschalter-Schnappschalter/dp/B0D6FNMY6R)         | 4        | Microswitch                  |
| [Raspberry Pi 4](https://www.amazon.de/Raspberry-Starter-Kit-Offizielles-Kühlkörper-USB-Kartenleser/dp/B0DZ8JYXGQ)           | 1        | Controller                   |
| [Arduino Nano](https://www.amazon.de/YELUFT-CH340G-Kompatibel-Arduino-Typ-C-Schnittstelle/dp/B0F5PZXH51)             | 1        | Optional low-level controller|
| [25KG Servo](https://www.amazon.de/APKLVSR-Digitaler-Servomotor-Getriebe-Hubschrauber/dp/B0D3DGRMRX)         | 1        | 180-360°                       |
| [Silicone Pads](https://www.amazon.de/Abeillo-Selbstklebend-Anti-Rutsch-Gummimatte-Rechteckige-Rutschhemmer/dp/B0B5R847RS)  | 2        | Gripper                      |
| [12V Power Supply](https://www.amazon.de/Netzteil-Schaltnetzteil-Transformator-Beleuchtung-Industrieanlagen/dp/B07BLR16PB)         | 1        | 5–10 A                       |
| [ATO/ATC](https://www.amazon.de/ELECTRAPICK-Sicherung-Sicherungen-Flachsicherungen-Automotive/dp/B09LQ8YPV6)| 1     |  |
| [ATO/ATC Block](https://www.amazon.de/Sicherungshalter-Sicherungskasten-Flachsicherungshalter-Schutzabdeckung-Sicherungsblock/dp/B0FCFSXWQ9) | 1     |  |

## Software
- **Python Scripts (Raspberry Pi):**
  - Grid map management and pathfinding (e.g., A*)  
  - Sensor reading (endstops, IMU)
  - Motor control
  - gripper actuation 
- **Optional:** ROS2 nodes for navigation and higher-level control  

## Assembly Instructions
1. Assemble the chassis (wheels, motors, frame)  
2. Mount the Z-lift mechanism  
3. Attach gripper arms to the Z-lift  
4. Place sensors (endstops, optional IMU)  
5. Wire motor drivers and sensors to Raspberry Pi / Arduino  
6. Upload Arduino firmware and test motor/sensor functionality  
7. Run Python scripts or ROS2 nodes to test autonomous movement  

## Testing & Calibration
- Verify endstop functionality  
- Calibrate grid steps (42 mm per cell)  
- Test Z-lift and gripper actuation  
- Adjust gripper force if using load-cell feedback  

## Optional Extensions
- RFID/NFC for box tracking  
- Camera for visual feedback  
- Multi-robot coordination  
- Automated charging station  

## License
MIT
