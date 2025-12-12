import time
import RPi.GPIO as GPIO

STEP_PIN = 17
DIR_PIN = 27
MICROSTEP_FACTOR = 1  # z.B. 16 für 1/16 Microstepping

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

def move_cell(degree, direction):
    steps = int(degree / 1.8 * MICROSTEP_FACTOR)
    GPIO.output(DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)
    for _ in range(steps):
        GPIO.output(STEP_PIN, True)
        time.sleep(0.001)
        GPIO.output(STEP_PIN, False)
        time.sleep(0.001)

try:
    move_cell(800, True)   # Richtung vorwärts
    time.sleep(1)
    move_cell(800, False)  # Richtung rückwärts
finally:
    GPIO.cleanup()
