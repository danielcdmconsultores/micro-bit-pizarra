x = 0
y = 0

def on_button_pressed_a():
    global x
    led.plot(x, y)
    x += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global y
    led.plot(x, y)
    y += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    global y
    global x
    x = 0
    y = 0
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)
