#SERVOS
#Port 1 (Rotation) - Right Drive
#Port 2 (Position) - Lift (Mouth)
#Port 3 - N/A
#Port 4 - (Rotation) - Left Drive

#SENSORS
#Port 1 (Ultrasonic Sensor) - HC-SR04

#TRI-COLOURS LEDS
#Port 1 - Right Eye
#Port 2 - lEft Eye

def scan(velL, velR, cmdistance):
    hummingbird.start_hummingbird()
    hummingbird.set_rotation_servo(FourPort.ONE, velR)
    hummingbird.set_rotation_servo(FourPort.FOUR, velL)
    while hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.ONE) > cmdistance:
        basic.pause(0.1)
    hummingbird.set_rotation_servo(FourPort.ONE, 0)
    hummingbird.set_rotation_servo(FourPort.FOUR, 0)
    
def movetoobject(velL, velR, cmdistance):
    hummingbird.start_hummingbird()
    hummingbird.set_rotation_servo(FourPort.ONE, velR)
    hummingbird.set_rotation_servo(FourPort.FOUR, velL)
    while hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.ONE) > cmdistance:
        basic.pause(0.1)
    hummingbird.set_rotation_servo(FourPort.ONE, 0)
    hummingbird.set_rotation_servo(FourPort.FOUR, 0)

def consume(velL, velR, liftRest, liftUp, cmdistance, R, G, B):
    hummingbird.start_hummingbird()
    Red = (R / 255) * 100
    Green = (G / 250) * 100
    Blue = (B / 250) * 100
    hummingbird.set_position_servo(FourPort.TWO, liftUp)
    hummingbird.set_tri_led(TwoPort.ONE, Red, Green, Blue)
    hummingbird.set_tri_led(TwoPort.TWO, Red, Green, Blue)
    hummingbird.set_rotation_servo(FourPort.ONE, velR)
    hummingbird.set_rotation_servo(FourPort.FOUR, velL)
    while hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.ONE) > cmdistance:
        basic.pause(0.1)
    hummingbird.set_rotation_servo(FourPort.ONE, 0)
    hummingbird.set_rotation_servo(FourPort.FOUR, 0)
    hummingbird.set_position_servo(FourPort.TWO, liftRest)
    hummingbird.set_tri_led(TwoPort.ONE, 100, 100, 100)
    hummingbird.set_tri_led(TwoPort.TWO, 100, 100, 100)

def object():
    hummingbird.set_position_servo(FourPort.TWO, 0)
    hummingbird.set_tri_led(TwoPort.ONE, 100, 100, 100)
    hummingbird.set_tri_led(TwoPort.TWO, 100, 100, 100)
    scan(20, 20, 4)
    consume(5, 5, 0, 30, 0, 120, 120, 120)

object()