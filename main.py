def on_forever():
    led.toggle(randint(0, 4), randint(0, 4))
    basic.pause(500)
basic.forever(on_forever)

def on_button_pressed_a():
    basic.show_string("A")
    servos.P1.set_angle(0)
    servos.P2.set_angle(180)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("B")
    servos.P1.set_angle(180)
    servos.P2.set_angle(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
strip.clear()
strip.show()
strip.show_rainbow(1, 360)
basic.pause(2000)
strip.clear()
strip.show()
