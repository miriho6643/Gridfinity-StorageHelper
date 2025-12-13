# Wiring Guide – Gridfinity Autopilot

## 1️⃣ Overview of Main Components
- **[Stepper Motors (NEMA17)](https://www.omc-stepperonline.com/de/nema-17-bipolar-1-8deg-40ncm-0-4a-12v-42x42x39mm-4-draehte-17hs15-0404s)** – for X/Y movement and optional Z-lift  
- **[Motor Drivers (Pololu A4988)](https://www.amazon.de/AZDelivery-Schritt-komplett-Stiftleisten-Kühlkörper/dp/B07C2V9GWC)** – control stepper motors (heatsinks included)  
- **[Raspberry Pi 4](https://www.amazon.de/Raspberry-Starter-Kit-Offizielles-Kühlkörper-USB-Kartenleser/dp/B0DZ8JYXGQ)** – main controller (Python / ROS2)  
- **[Arduino Nano](https://www.amazon.de/YELUFT-CH340G-Kompatibel-Arduino-Typ-C-Schnittstelle/dp/B0F5PZXH51)** – optional: low-level stepper control  
- **[Endstop Switches](https://www.amazon.de/JZK-Mikroschalter-Mikro-Endschalter-Scharnierhebelschalter-Schnappschalter/dp/B0D6FNMY6R)** – for home positions  
- **Mini Linear Actuator / Gummiarme** – Z-lift and gripper actuation  
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

> ⚠️ Set motor current (VREF) properly to avoid overheating.  
> ⚠️ If using microstepping (e.g., 1/16), multiply steps accordingly in your scripts.

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
- I2C devices (IMU, ToF) → GPIO2 (SDA), GPIO3 (SCL)

> ⚠️ Pull-up resistor (10kΩ) if using NC switches; can also enable internal pull-up on Raspberry Pi GPIO.

---

## 4️⃣ Endstops / Sensors
- Home sensors X/Y/Z → digital GPIO input  
- Pull-up resistor (10kΩ) if using NC switches  
- Optional IMU → I2C bus  

---

## 5️⃣ Z-Lift & Gripper
- Linear actuator → PWM pin (Arduino)  
- Gripper servo → PWM pin (Arduino)  
- Connect GND to common ground  

---

## 6️⃣ Power Supply
- **12V** → stepper drivers, linear actuator  
- **5V** → Raspberry Pi (via USB-C or DC-DC step-down converter)  
- All GNDs must be connected together  

### ASCII Power & Wiring Overview
12V PSU --> Motor Drivers --> Steppers
--> Linear Actuator
--> GND common
5V PSU --> Raspberry Pi
GND --> shared among all

---

## 7️⃣ Example Wiring Sketch (Text Diagram)
Raspberry Pi GPIO 17 ---> STEP Pin X-Driver
Raspberry Pi GPIO 27 ---> DIR Pin X-Driver
Raspberry Pi GPIO 22 ---> STEP Pin Y-Driver
Raspberry Pi GPIO 23 ---> DIR Pin Y-Driver

Arduino D2 ---> STEP Pin Z-Driver
Arduino D3 ---> DIR Pin Z-Driver

Endstop X-min ---> GPIO 5 (Pull-up)
Endstop Y-min ---> GPIO 6 (Pull-up)
Endstop Z-min ---> GPIO 7 (Pull-up)

ToF Sensor SDA/SCL ---> GPIO2/GPIO3 (I2C)
Z-Lift Linear Actuator ---> PWM Pin D9 Arduino
Gripper Servo ---> PWM Pin D10 Arduino

12V Power Supply --> Drivers / Linear Actuator
5V Power Supply --> Raspberry Pi
GND --> All components connected together
