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
    for _ in range(abs(dx) * STEPPER_MULTIPLYER * 1.8):
        GPIO.output(STEPX_PIN, True)
        time.sleep(0.001)
        GPIO.output(STEPX_PIN, False)
        time.sleep(0.001)

    # Y-axis
    GPIO.output(DIRY_PIN, dy >= 0)
    for _ in range(abs(dy) * STEPPER_MULTIPLYER * 1.8):
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
        for _ in range(Z_HEIGHT-CELL_HEIGHT*SERVO_MULTIPLYER*1.8):
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
    """Placeholder for calibration routine"""
    pass

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
        move_cell((0, 0), (1, 1))
    except KeyboardInterrupt:
        stop()
