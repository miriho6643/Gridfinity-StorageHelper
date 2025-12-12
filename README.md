# Gridfinity Autopilot

## Beschreibung
Autonomer Roboter zum Bewegen von Gridfinity-Boxen auf 42x42mm Raster.  
Differential Drive + Z-Hub + Greifer mit Druckarmen.

## Hardware
- NEMA17 Stepper Motor 40 Ncm
- TB6600 Stepper-Treiber oder Pololu A4988
- Raspberry Pi 4
- Arduino Nano / Uno (optional)
- Mikroschalter Endschalter
- ToF Sensor VL53L1X
- Mini Linearaktuator für Z-Hub
- Gummiarme für Greifer

## Software
- Arduino Sketch für Low-Level-Motorsteuerung
- Python-Skripte auf Raspberry Pi:
  - Grid-Map Verwaltung
  - Motion Controller
  - Sensor-Abfragen (Endschalter, ToF, IMU)
- Optional ROS2 Nodes

## Aufbau
1. Mechanik montieren (Chassis, Z-Hub, Greifer)
2. Sensoren platzieren
3. Verkabelung aufbauen
4. Arduino Firmware laden
5. Python-Skripte starten / ROS2 Nodes starten
6. Testen und kalibrieren

## Test & Kalibrierung
- Endschalter prüfen
- Schrittgröße 42 mm testen
- Z-Hub & Greifer prüfen
- Kraftregelung testen

## Erweiterungen
- RFID / NFC Inventartracking
- Kamera für visuelle Kontrolle
- Multi-Roboter Koordination

## Lizenz
MIT
