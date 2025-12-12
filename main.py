# This file is written for the Raspberry Pi 4 zero

import time
import RPi.GPIO as GPIO

STEP = 17
DIR  = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)

def move(steps, direction):
    GPIO.output(DIR, direction)
    for _ in range(steps):
        GPIO.output(STEP, True)
        time.sleep(0.001)
        GPIO.output(STEP, False)
        time.sleep(0.001)

try:
    move(1000, True)  # vorwärts
    time.sleep(1)
    move(1000, False) # rückwärts
finally:
    GPIO.cleanup()
