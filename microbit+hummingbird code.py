# SERVOS
# Port 1 (Rotation) - left Drive
# Port 2 (Position) - Lift Left
# Port 3 - (Position) - Lift Right
# Port 4 - (Rotation) - Right Drive
# SENSORS
# Port 1 (Ultrasonic Sensor) - HC-SR04
# TRI-COLOURS LEDS
# Port 1 - Left Eye
# Port 2 - Right Eye

def scan(velL, velR, cmdistance): # Function for scanning objects
    hummingbird.start_hummingbird() # Initialize hummingbird
    hummingbird.set_rotation_servo(FourPort.ONE, velL) # Set left & right drive motor to specificed speed
    hummingbird.set_rotation_servo(FourPort.FOUR, velR)
    while hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.ONE) > cmdistance: # Exit loop once target distance is reached
        basic.pause(0.1) # Pause for 0.1 milisecond
    hummingbird.set_rotation_servo(FourPort.ONE, 0) # Set left & right drive motor to 0
    hummingbird.set_rotation_servo(FourPort.FOUR, 0)

def movetoobject(velL, velR, cmdistance): # Function for moving to an object
    hummingbird.start_hummingbird() # Initialize hummingbird
    hummingbird.set_rotation_servo(FourPort.ONE, velL) # Set left & right drive motor to specificed speed
    hummingbird.set_rotation_servo(FourPort.FOUR, velR)
    while hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.ONE) > cmdistance:  # Exit loop once target distance is reached
        basic.pause(0.1) # Pause for 0.1 milisecond
    hummingbird.set_rotation_servo(FourPort.ONE, 0) # Set left & right drive motor to 0
    hummingbird.set_rotation_servo(FourPort.FOUR, 0)

def consume(velL, velR, liftL, liftR, R, G, B): # Function for biting the object
    hummingbird.start_hummingbird() # Initialize hummingbird
    hummingbird.set_tri_led(TwoPort.ONE, R, G, B) # Set left and right tri-leds to specificed RGB values
    hummingbird.set_tri_led(TwoPort.TWO, R, G, B)
    hummingbird.set_position_servo(FourPort.TWO, 0) # Set left and right drive motor to 0 degrees
    hummingbird.set_position_servo(FourPort.THREE, 0)
    basic.pause(5000) # Pause for 5 seconds
    hummingbird.set_tri_led(TwoPort.ONE, 100, 100, 100) # Set left and right tri-leds to white
    hummingbird.set_tri_led(TwoPort.TWO, 100, 100, 100)
    hummingbird.set_position_servo(FourPort.TWO, 180) # Set left lift motor to 180 degrees
    hummingbird.set_position_servo(FourPort.THREE, -180) # Set right lift motor to -180 degrees
    hummingbird.set_rotation_servo(FourPort.ONE, velL)  # Set left and right drive motor to specified speed
    hummingbird.set_rotation_servo(FourPort.FOUR, velR)
    basic.pause(2000) # Pause for 2 seconds
    hummingbird.set_rotation_servo(FourPort.ONE, 0) # Set left and right drive motor to 0
    hummingbird.set_rotation_servo(FourPort.FOUR, 0)

def object(): # Function for scanning, moving, and consuming an object
    hummingbird.start_hummingbird() # Initialize hummingbird
    scan(50, 50, 55)
    movetoobject(102, -100, 17)
    consume(-60,40,150,30,100,0,0)

basic.show_leds("""
    # # # # #
    # . . . .
    # . # # #
    # . . . #
    # # # # #
    """)
basic.pause(5000) # Pause for 5 seconds
hummingbird.set_tri_led(TwoPort.ONE, 100, 100, 100) # Set left and right tri-leds to white
hummingbird.set_tri_led(TwoPort.TWO, 100, 100, 100)
object()
basic.show_leds("""
    # # # . .
    # . . # .
    # . . . #
    # . . # .
    # # # . .
    """)
