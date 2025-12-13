import time
import RPi.GPIO as GPIO

STEPX_PIN = 17
DIRX_PIN = 27

STEPY_PIN = 16
DIRY_PIN = 26

GRIPPER_PIN = 15
ZAXE_PIN = 25

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
