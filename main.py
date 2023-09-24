def on_bluetooth_connected():
    pass
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    pass
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    keyboard.send_string(" ")
    basic.show_leds("""
        . . # . .
        . # # # .
        . . . . .
        . . . . .
        . . # . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    basic.show_leds("""
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        """)
    mouse.movexy(-5, 0)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_six_g():
    mouse.click()
    basic.show_icon(IconNames.STICK_FIGURE)
    music.play(music.create_sound_expression(WaveShape.SAWTOOTH,
            2987,
            2882,
            255,
            0,
            500,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

def my_function():
    if mouse.is_enabled():
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SMALL_DIAMOND)
mouse.set_status_change_handler(my_function)

def my_function2():
    if keyboard.is_enabled():
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SMALL_DIAMOND)
keyboard.set_status_change_handler(my_function2)

def on_button_pressed_b():
    keyboard.send_string("w")
    basic.show_leds("""
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    basic.show_leds("""
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        """)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

mouse.start_mouse_service()
keyboard.start_keyboard_service()

def on_forever():
    pass
basic.forever(on_forever)
