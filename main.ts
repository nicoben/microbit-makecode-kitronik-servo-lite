basic.forever(function on_forever() {
    led.toggle(randint(0, 4), randint(0, 4))
    basic.pause(500)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("A")
    servos.P1.setAngle(0)
    servos.P2.setAngle(180)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("B")
    servos.P1.setAngle(180)
    servos.P2.setAngle(0)
})
let strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
strip.clear()
strip.show()
strip.showRainbow(1, 360)
basic.pause(2000)
strip.clear()
strip.show()
