function movetoobject(velL: number, velR: number, time: number) {
    hummingbird.startHummingbird()
    hummingbird.setRotationServo(FourPort.One, velL)
    hummingbird.setRotationServo(FourPort.Four, velR)
    basic.pause(time)
    hummingbird.setRotationServo(FourPort.One, 0)
    hummingbird.setRotationServo(FourPort.Four, 0)
}

//  SERVOS
//  Port 1 (Rotation) - Right Drive
//  Port 2 (Position) - Lift Right
//  Port 3 - (Position) - Lift Left
//  Port 4 - (Rotation) - Left Drive
//  SENSORS
//  Port 1 (Ultrasonic Sensor) - HC-SR04
//  TRI-COLOURS LEDS
//  Port 1 - Right Eye
//  Port 2 - Left Eye
function scan(velL: number, velR: number, time: number) {
    hummingbird.startHummingbird()
    hummingbird.setRotationServo(FourPort.One, velL)
    hummingbird.setRotationServo(FourPort.Four, velR)
    basic.pause(time)
    hummingbird.setRotationServo(FourPort.One, 0)
    hummingbird.setRotationServo(FourPort.Four, 0)
}

function consume(velL: number, velR: number, liftL: number, liftR: number, time: number, R: number, G: number, B: number) {
    hummingbird.startHummingbird()
    hummingbird.setTriLED(TwoPort.One, R, G, B)
    hummingbird.setTriLED(TwoPort.Two, R, G, B)
    hummingbird.setPositionServo(FourPort.Two, 0)
    hummingbird.setPositionServo(FourPort.Three, 0)
    basic.pause(time)
    hummingbird.setTriLED(TwoPort.One, 100, 100, 100)
    hummingbird.setTriLED(TwoPort.Two, 100, 100, 100)
    hummingbird.setPositionServo(FourPort.Two, 180)
    hummingbird.setPositionServo(FourPort.Three, -180)
    hummingbird.setRotationServo(FourPort.One, velL)
    hummingbird.setRotationServo(FourPort.Four, velR)
    basic.pause(2000)
    hummingbird.setRotationServo(FourPort.One, 0)
    hummingbird.setRotationServo(FourPort.Four, 0)
}

hummingbird.startHummingbird()
basic.showLeds(`
    # # # # #
    # . . . .
    # . # # #
    # . . . #
    # # # # #
    `)
basic.pause(5000)
hummingbird.setTriLED(TwoPort.One, 100, 100, 100)
hummingbird.setTriLED(TwoPort.Two, 100, 100, 100)
scan(50, 50, 1600)
hummingbird.setTriLED(TwoPort.One, 100, 100, 100)
hummingbird.setTriLED(TwoPort.Two, 100, 100, 100)
movetoobject(102, -100, 3000)
hummingbird.setTriLED(TwoPort.One, 100, 100, 100)
hummingbird.setTriLED(TwoPort.Two, 100, 100, 100)
consume(-60, 40, 150, 30, 5000, 100, 0, 0)
basic.showLeds(`
    # # # . .
    # . . # .
    # . . . #
    # . . # .
    # # # . .
    `)
