# Gridfinity Autopilot

## Description
An autonomous robot designed to move Gridfinity boxes on a 42x42 mm grid.  
The robot features a differential drive, a Z-lift mechanism, and a gripper with pressure arms.

## Hardware
- **Motors:** NEMA17 Stepper Motor 40 Ncm  
- **Motor Drivers:** TB6600 Stepper Driver or Pololu A4988  
- **Controller:** Raspberry Pi 4  
- **Optional Microcontroller:** Arduino Nano / Uno for low-level motor control  
- **Sensors:** Microswitch endstops, VL53L1X ToF distance sensor  
- **Actuators:** Mini linear actuator for Z-lift, rubber/silicone gripper arms  

## Software
- **Arduino Sketch:** Low-level motor control, Z-lift, gripper actuation, endstop reading  
- **Python Scripts (Raspberry Pi):**
  - Grid map management and pathfinding (e.g., A*)  
  - Motion controller sending STEP/DIR commands to Arduino  
  - Sensor reading (endstops, IMU)  
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
