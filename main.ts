let x = 0
let y = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    led.plot(x, y)
    x += 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    led.plot(x, y)
    y += 1
})
input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touched() {
    
    
    x = 0
    y = 0
})
