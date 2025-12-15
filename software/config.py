# Gridfinity System Configuration

# Grid dimensions
GRID_ROWS = 40        # Anzahl Reihen (angepasst für kleines Lager)
GRID_COLS = 40        # Anzahl Spalten
GRID_STORAGES = 10   # Anzahl der Lagerboxen

# Grid cell dimensions (mm)
CELL_WIDTH = 42      # Breite einer Gridfinity-Zelle, z.B. Standard-Gridfinity-Modul
CELL_HEIGHT = 42     # Tiefe einer Gridfinity-Zelle
Z_HEIGHT = 50        # max Höhe Z-Lift (mm)

# Movement multipliers
STEPPER_MULTIPLIER = 16  # für 1/16 Microstepping bei A4988

# Stepper motor pins (BCM)
STEPX_PIN = 17
DIRX_PIN = 27
STEPY_PIN = 23
DIRY_PIN = 24
STEPZ_PIN = 5
DIRZ_PIN = 6

# Gripper servo pin
GRIPPER_PIN = 19

# Endstop pins (BCM)
XEND_PIN = 16
YEND_PIN = 20
ZEND_PIN = 21
