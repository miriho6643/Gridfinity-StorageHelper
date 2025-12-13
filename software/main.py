import time
import RPi.GPIO as GPIO
from config import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN,GPIO.OUT)
GPIO.setup(DIR_PIN,GPIO.OUT)

def move_cell(steps,axe,direction):
    GPIO.output(DIR_PIN,direction)
    for _ in range(steps):
        GPIO.output(STEP_PIN,True)
        time.sleep(0.001)
        GPIO.output(STEP_PIN,False)
        time.sleep(0.001)

def home(x: bool = True, y: bool = True, z: bool = True):
    pass
    
try:
    move_cell(800,True)
    time.sleep(1)
    move_cell(800,False)
finally:
    GPIO.cleanup()
