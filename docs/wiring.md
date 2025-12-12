# Wiring Guide – Gridfinity Autopilot

## 1️⃣ Overview of Main Components
- **Stepper Motors (NEMA17)** – for X/Y movement and optional Z-lift  
- **Motor Drivers (Pololu A4988 or TB6600)** – control stepper motors  
- **Raspberry Pi 4** – main controller (Python / ROS2)  
- **Arduino Nano** – optional: low-level stepper control  
- **Endstops / Microswitches** – for home positions  
- **ToF Sensor (VL53L1X)** – for precise positioning  
- **Linear Actuator / Gripper** – Z-lift and gripper actuation  
- **12V Power Supply** – powers steppers and actuators  

---

## 2️⃣ Stepper Motor Wiring

| Connection | Stepper Cable |
|------------|---------------|
| A+         | Red           |
| A-         | Blue          |
| B+         | Green         |
| B-         | Black         |

**Driver → Controller**

- **STEP** → GPIO pin from Arduino/RPi  
- **DIR** → GPIO pin from Arduino/RPi  
- **Enable** → optional, LOW to activate  
- **GND** → connect to controller GND  
- **Vmot** → 12V power supply  

> ⚠️ Set motor current on driver (VREF) properly to avoid overheating.

---

## 3️⃣ Arduino / Raspberry Pi Wiring

### a) Arduino
- STEP/DIR pins → Motor Driver  
- Endstops → digital pins + GND  
- Optional: PWM pins for Z-lift / gripper  
- Connect Arduino GND to driver and power supply GND  

### b) Raspberry Pi
- GPIO → STEP/DIR driver pins  
- Logic level: Pi uses 3.3V; driver may require 5V → use level shifter if needed  
- Endstops → GPIO with pull-up/down resistor  
- I2C devices (ToF, IMU) → GPIO2 (SDA), GPIO3 (SCL)  

---

## 4️⃣ Endstops / Sensors
- Home sensors X/Y/Z → digital GPIO input  
- Pull-up resistor (10kΩ) if using NC switches  
- ToF sensor → I2C bus  
- Optional IMU → I2C bus  

---

## 5️⃣ Z-Lift & Gripper
- Linear actuator → PWM pin (Arduino)  
- Gripper servo → PWM pin (Arduino)  
- Connect GND to common ground  

---

## 6️⃣ Power Supply
- 12V → stepper drivers and linear actuator  
- 5V → Raspberry Pi (via USB-C or DC-DC)  
- All GNDs must be connected together  

---

## 7️⃣ Example Wiring Sketch (Text Diagram)
