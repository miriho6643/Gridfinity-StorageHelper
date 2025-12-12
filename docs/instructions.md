# Assembly Instructions

## Step 1: Assemble the Chassis
- Install wheels, linear rails, or sliders (depending on design).
- Mount the stepper motors for X, Y and Z movement.
- Ensure the frame is rigid and square.

## Step 2: Mount the Z-Lift Mechanism
- Attach the linear actuator or Z-slide.
- Verify smooth vertical movement.
- Ensure the Z-lift can carry the weight of a full Gridfinity bin.

## Step 3: Attach the Gripper Arms
- Install the inverted gripper or rubber-pad arms.
- Verify closing/opening movement.
- Make sure the gripper can reliably grab and lift a Gridfinity box.

## Step 4: Install Sensors
- Mount all endstop switches for X, Y, and Z homing.
- Install the VL53L1X ToF distance sensor.
- Optionally add an IMU for movement stabilization.

## Step 5: Wire All Components
- Connect stepper drivers, motors, and endstops.
- Connect the Raspberry Pi or Arduino.
- Ensure all GND lines are shared.
- Double-check polarity and driver VREF settings.

## Step 6: Upload Firmware
- Flash the Arduino firmware.
- Test basic movements (step, direction, homing).
- Confirm the Z-lift and gripper actuate correctly.

## Step 7: Run Control Software
- Start Python scripts or ROS2 nodes on the Raspberry Pi.
- Test communication with the Arduino.
- Perform basic grid movements and coordinate commands.

## Step 8: Calibrate the System
- Calibrate X/Y steps per cell (Gridfinity pitch = 42 mm).
- Set Z-lift heights.
- Adjust gripper force and timing.
- Save calibration values in the config file.

