// SERVOS
// Port 1 (Rotation) - Right Drive
// Port 2 (Position) - Lift (Mouth)
// Port 3 - N/A
// Port 4 - (Rotation) - Left Drive
// SENSORS
// Port 1 (Ultrasonic Sensor) - HC-SR04
// TRI-COLOURS LEDS
// Port 1 - Right Eye
// Port 2 - lEft Eye
function scan(velL: number, velR: number, cmdistance: number) {
    hummingbird.startHummingbird()
    hummingbird.setRotationServo(FourPort.One, velR)
    hummingbird.setRotationServo(FourPort.Four, velL)
    while (hummingbird.getSensor(SensorType.Distance, ThreePort.One) > cmdistance) {
        basic.pause(0.1)
    }
    hummingbird.setRotationServo(FourPort.One, 0)
    hummingbird.setRotationServo(FourPort.Four, 0)
}

function movetoobject(velL: number, velR: number, cmdistance: any) {
    hummingbird.startHummingbird()
    hummingbird.setRotationServo(FourPort.One, velR)
    hummingbird.setRotationServo(FourPort.Four, velL)
    while (hummingbird.getSensor(SensorType.Distance, ThreePort.One) > cmdistance) {
        basic.pause(0.1)
    }
    hummingbird.setRotationServo(FourPort.One, 0)
    hummingbird.setRotationServo(FourPort.Four, 0)
}

function consume(velL: number, velR: number, liftRest: number, liftUp: number, cmdistance: number, R: number, G: number, B: number) {
    hummingbird.startHummingbird()
    let Red = R / 255 * 100
    let Green = G / 250 * 100
    let Blue = B / 250 * 100
    hummingbird.setPositionServo(FourPort.Two, liftUp)
    hummingbird.setTriLED(TwoPort.One, Red, Green, Blue)
    hummingbird.setTriLED(TwoPort.Two, Red, Green, Blue)
    hummingbird.setRotationServo(FourPort.One, velR)
    hummingbird.setRotationServo(FourPort.Four, velL)
    while (hummingbird.getSensor(SensorType.Distance, ThreePort.One) > cmdistance) {
        basic.pause(0.1)
    }
    hummingbird.setRotationServo(FourPort.One, 0)
    hummingbird.setRotationServo(FourPort.Four, 0)
    hummingbird.setPositionServo(FourPort.Two, liftRest)
    hummingbird.setTriLED(TwoPort.One, 100, 100, 100)
    hummingbird.setTriLED(TwoPort.Two, 100, 100, 100)
}

function object() {
    hummingbird.setPositionServo(FourPort.Two, 0)
    hummingbird.setTriLED(TwoPort.One, 100, 100, 100)
    hummingbird.setTriLED(TwoPort.Two, 100, 100, 100)
    scan(20, 20, 4)
    consume(5, 5, 0, 30, 0, 120, 120, 120)
}

object()
