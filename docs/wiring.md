## 1️⃣ Overview of Main Components
- **[Stepper Motors (NEMA17)](https://www.omc-stepperonline.com/de/nema-17-bipolar-1-8deg-40ncm-0-4a-12v-42x42x39mm-4-draehte-17hs15-0404s)** – X/Y/Z movement  
- **[A4988 Drivers](https://www.amazon.de/AZDelivery-Schritt-komplett-Stiftleisten-Kühlkörper/dp/B07C2V9GWC)** – stepper motor control (heatsinks included)  
- **Raspberry Pi 4** – main controller (Python / ROS2)  
- **[Endstop Switches](https://www.amazon.de/JZK-Mikroschalter-Mikro-Endschalter-Scharnierhebelschalter-Schnappschalter/dp/B0D6FNMY6R)** – for X/Y/Z home positions  
- **Linear actuator / 25KG Servo** – Z-lift & gripper  
- **12V Power Supply** – powers stepper drivers and actuators  

---

## 2️⃣ Stepper Motor Wiring

| Connection | Stepper Cable |
|------------|---------------|
| A+         | Red           |
| A-         | Blue          |
| B+         | Green         |
| B-         | Black         |

**Driver → Raspberry Pi (BCM GPIO)**

| Driver   | STEP   | DIR    | Enable (optional) |
|----------|--------|--------|------------------|
| X-Driver | GPIO17 | GPIO27 | GPIO22           |
| Y-Driver | GPIO23 | GPIO24 | GPIO25           |
| Z-Driver | GPIO5  | GPIO6  | GPIO12           |

- **GND** of driver → Raspberry Pi GND  
- **Vmot** → 12V Power Supply  

> ⚠️ Set motor current (VREF) properly to avoid overheating.  
> ⚠️ For microstepping, multiply steps in your code.

---

## 3️⃣ Endstops / Sensors

| Axis | Endstop | GPIO (BCM) | Pull |
|------|---------|------------|------|
| X    | Min     | GPIO16     | Pull-up |
| Y    | Min     | GPIO20     | Pull-up |
| Z    | Min     | GPIO21     | Pull-up |

- Connect one side of the switch to **GPIO**, the other to **GND**.  
- Enable internal pull-up in software (`GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)`).

---

## 4️⃣ Z-Lift & Gripper

| Component | GPIO (BCM) | Notes |
|-----------|------------|-------|
| Linear actuator (PWM) | GPIO18 | Hardware PWM (Raspberry Pi 4) |
| 25KG Servo | GPIO19 | Software PWM possible |

- **GND of actuator/servo** → common Raspberry Pi GND  

> ⚠️ Linear actuator may require extra driver or transistor to switch 12V safely.

---

## 5️⃣ Power Supply

- **12V → Stepper Drivers & Linear Actuator**  
- **5V → Raspberry Pi** (via USB-C or DC-DC step-down converter)  
- **All GNDs connected together**  

### ASCII Power & Wiring Overview

12V PSU --> Stepper Drivers --> Steppers
--> Linear Actuator
--> shared GND
5V PSU --> Raspberry Pi
GND -----> connected to all

---

## 6️⃣ Example Wiring Sketch (Text Diagram)

Stepper X: STEP GPIO17 ---> STEP
DIR GPIO27 ---> DIR
ENABLE GPIO22 ---> ENABLE

Stepper Y: STEP GPIO23 ---> STEP
DIR GPIO24 ---> DIR
ENABLE GPIO25 ---> ENABLE

Stepper Z: STEP GPIO5 ---> STEP
DIR GPIO6 ---> DIR
ENABLE GPIO12 ---> ENABLE

Endstops:
X-min --> GPIO16 (Pull-up)
Y-min --> GPIO20 (Pull-up)
Z-min --> GPIO21 (Pull-up)

Z-Lift Linear Actuator --> GPIO18 (PWM, via transistor/driver)
Gripper Servo --> GPIO19 (PWM)

12V Power Supply --> Drivers / Linear Actuator
5V Power Supply --> Raspberry Pi
GND --> All components connected together

---

## Notes

- Make sure all **grounds are connected together**.  
- Check **motor current VREF** before running.  
- If using microstepping (1/16, 1/8), adjust step counts in software.  
- For the actuator, use a **driver transistor or MOSFET** to handle 12V/5–10A safely.  
- Pull-ups for endstops can be enabled in software; no external resistor needed if using Pi internal pull-ups.
