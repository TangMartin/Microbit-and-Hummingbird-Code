def movetoobject(velL: number, velR: number, time: number):
    hummingbird.start_hummingbird()
    hummingbird.set_rotation_servo(FourPort.ONE, velL)
    hummingbird.set_rotation_servo(FourPort.FOUR, velR)
    basic.pause(time)
    hummingbird.set_rotation_servo(FourPort.ONE, 0)
    hummingbird.set_rotation_servo(FourPort.FOUR, 0)
# SERVOS
# Port 1 (Rotation) - Right Drive
# Port 2 (Position) - Lift Right
# Port 3 - (Position) - Lift Left
# Port 4 - (Rotation) - Left Drive
# SENSORS
# Port 1 (Ultrasonic Sensor) - HC-SR04
# TRI-COLOURS LEDS
# Port 1 - Right Eye
# Port 2 - Left Eye
def scan(velL: number, velR: number, time: number):
    hummingbird.start_hummingbird()
    hummingbird.set_rotation_servo(FourPort.ONE, velL)
    hummingbird.set_rotation_servo(FourPort.FOUR, velR)
    basic.pause(time)
    hummingbird.set_rotation_servo(FourPort.ONE, 0)
    hummingbird.set_rotation_servo(FourPort.FOUR, 0)
def consume(velL: number, velR: number, liftL: number, liftR: number, time: number, R: number, G: number, B: number):
    hummingbird.start_hummingbird()
    hummingbird.set_tri_led(TwoPort.ONE, R, G, B)
    hummingbird.set_tri_led(TwoPort.TWO, R, G, B)
    hummingbird.set_position_servo(FourPort.TWO, 0)
    hummingbird.set_position_servo(FourPort.THREE, 0)
    basic.pause(time)
    hummingbird.set_tri_led(TwoPort.ONE, 100, 100, 100)
    hummingbird.set_tri_led(TwoPort.TWO, 100, 100, 100)
    hummingbird.set_position_servo(FourPort.TWO, 180)
    hummingbird.set_position_servo(FourPort.THREE, -180)
    hummingbird.set_rotation_servo(FourPort.ONE, velL)
    hummingbird.set_rotation_servo(FourPort.FOUR, velR)
    basic.pause(2000)
    hummingbird.set_rotation_servo(FourPort.ONE, 0)
    hummingbird.set_rotation_servo(FourPort.FOUR, 0)
hummingbird.start_hummingbird()
basic.show_leds("""
    # # # # #
    # . . . .
    # . # # #
    # . . . #
    # # # # #
    """)
basic.pause(5000)
hummingbird.set_tri_led(TwoPort.ONE, 100, 100, 100)
hummingbird.set_tri_led(TwoPort.TWO, 100, 100, 100)
scan(50, 50, 1600)
hummingbird.set_tri_led(TwoPort.ONE, 100, 100, 100)
hummingbird.set_tri_led(TwoPort.TWO, 100, 100, 100)
movetoobject(102, -100, 3000)
hummingbird.set_tri_led(TwoPort.ONE, 100, 100, 100)
hummingbird.set_tri_led(TwoPort.TWO, 100, 100, 100)
consume(-60,40,150,30,5000,100,0,0)
basic.show_leds("""
    # # # . .
    # . . # .
    # . . . #
    # . . # .
    # # # . .
    """)

