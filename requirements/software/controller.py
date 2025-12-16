import time
import RPi.GPIO as GPIO
from config import *

# -------------------------------
# GLOBAL VARIABLES
# -------------------------------
pos = [0, 0]  # aktuelle X/Y-Position
storages = [None for _ in range(GRID_STORAGES)]

GPIO.setmode(GPIO.BCM)

# Stepper Pins Setup
GPIO.setup(STEPX_PIN, GPIO.OUT)
GPIO.setup(DIRX_PIN, GPIO.OUT)

GPIO.setup(STEPY_PIN, GPIO.OUT)
GPIO.setup(DIRY_PIN, GPIO.OUT)

GPIO.setup(STEPZ_PIN, GPIO.OUT)
GPIO.setup(DIRZ_PIN, GPIO.OUT)

# Endstops als Input (optional)
GPIO.setup(XEND_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(YEND_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ZEND_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Gripper Servo Setup
GPIO.setup(GRIPPER_PIN, GPIO.OUT)
pwm = GPIO.PWM(GRIPPER_PIN, 50)
pwm.start(0)

# -------------------------------
# GRID / CELLS CLASS
# -------------------------------
class Cells:
    def __init__(self):
        self._cells = [
            [None for _ in range(GRID_COLS)]
            for _ in range(GRID_ROWS)
        ]

    @property
    def cellnames(self):
        return self._cells

    def set_cell(self, cell: tuple, name: str):
        x, y = cell
        if not (0 <= x < GRID_COLS and 0 <= y < GRID_ROWS):
            raise IndexError("Cell out of grid range")
        self._cells[y][x] = name

    def get_cell(self, cell: tuple):
        x, y = cell
        if not (0 <= x < GRID_COLS and 0 <= y < GRID_ROWS):
            raise IndexError("Cell out of grid range")
        return self._cells[y][x]

    @cellnames.deleter
    def cellnames(self):
        for y in range(GRID_ROWS):
            for x in range(GRID_COLS):
                self._cells[y][x] = None

# -------------------------------
# STEPPER MOVEMENT
# -------------------------------
def move(to: tuple):
    """
    Moves the X/Y steppers to the target position.
    'to' is a tuple of (x, y) in cells.
    """
    global pos
    x, y = to
    dx = x - pos[0]
    dy = y - pos[1]

    # X-axis
    GPIO.output(DIRX_PIN, dx >= 0)
    for _ in range(int(abs(dx) * STEPPER_MULTIPLIER * 1.8)):
        GPIO.output(STEPX_PIN, True)
        time.sleep(0.001)
        GPIO.output(STEPX_PIN, False)
        time.sleep(0.001)

    # Y-axis
    GPIO.output(DIRY_PIN, dy >= 0)
    for _ in range(int(abs(dy) * STEPPER_MULTIPLIER * 1.8)):
        GPIO.output(STEPY_PIN, True)
        time.sleep(0.001)
        GPIO.output(STEPY_PIN, False)
        time.sleep(0.001)

    pos[0], pos[1] = x, y

# -------------------------------
# GRIPPER CLASS
# -------------------------------
class Gripper:
    @staticmethod
    def open(is_open: bool):
        angle = 0 if is_open else 90
        duty = 2 + angle / 18
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.4)
        pwm.ChangeDutyCycle(0)

    @staticmethod
    def move_z(up: bool):
        GPIO.output(DIRZ_PIN, up)
        for _ in range(int(Z_HEIGHT-CELL_HEIGHT*STEPPER_MULTIPLIER*1.8)):
            GPIO.output(STEPZ_PIN, True)
            time.sleep(0.001)
            GPIO.output(STEPZ_PIN, False)
            time.sleep(0.001)

    @staticmethod
    def take():
        Gripper.move_z(False)
        Gripper.open(False)
        Gripper.move_z(True)

    @staticmethod
    def place():
        Gripper.move_z(False)
        Gripper.open(True)
        Gripper.move_z(True)

# -------------------------------
# HIGH LEVEL MOVEMENT
# -------------------------------
def move_cell(origin: tuple, to: tuple):
    """
    Move a cell from origin to destination
    'origin' and 'to' are (x, y) tuples.
    """
    move(origin)
    Gripper.take()
    move(to)
    Gripper.place()

# -------------------------------
# UTILITY
# -------------------------------
def calibrate(x: bool = True, y: bool = True, z: bool = True):
    """Kalibrierung aller Achsen zu den Endstops"""
    
    print("Starte Kalibrierung...")
    
    # X-Achse homing
    if x:
        print("Fahre X-Achse zum Endstop...")
        GPIO.output(DIRX_PIN, False)  # Richtung Endstop
        while GPIO.input(XEND_PIN) == GPIO.HIGH:
            GPIO.output(STEPX_PIN, True)
            time.sleep(0.002)
            GPIO.output(STEPX_PIN, False)
            time.sleep(0.002)
        pos[0] = 0
        print("X-Achse kalibriert.")

    # Y-Achse homing
    if y:
        print("Fahre Y-Achse zum Endstop...")
        GPIO.output(DIRY_PIN, False)
        while GPIO.input(YEND_PIN) == GPIO.HIGH:
            GPIO.output(STEPY_PIN, True)
            time.sleep(0.002)
            GPIO.output(STEPY_PIN, False)
            time.sleep(0.002)
        pos[1] = 0
        print("Y-Achse kalibriert.")

    # Z-Achse homing
    if z:
        print("Fahre Z-Achse zum Endstop...")
        GPIO.output(DIRZ_PIN, False)
        while GPIO.input(ZEND_PIN) == GPIO.HIGH:
            GPIO.output(STEPZ_PIN, True)
            time.sleep(0.002)
            GPIO.output(STEPZ_PIN, False)
            time.sleep(0.002)
        print("Z-Achse kalibriert.")

    print("Alle ausgewählten Achsen kalibriert!")

def stop():
    """Cleanup GPIO and stop PWM"""
    pwm.stop()
    GPIO.cleanup()
    exit()

# -------------------------------
# EXAMPLE USAGE
# -------------------------------
if __name__ == "__main__":
    grid = Cells()
    grid.set_cell((0, 0), "TestBox")

    try:
        calibrate()
    except KeyboardInterrupt:
        stop()
