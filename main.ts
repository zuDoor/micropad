bluetooth.onBluetoothConnected(function () {
	
})
bluetooth.onBluetoothDisconnected(function () {
	
})
input.onButtonPressed(Button.A, function () {
    keyboard.sendString(" ")
    basic.showLeds(`
        . . # . .
        . # # # .
        . . . . .
        . . . . .
        . . # . .
        `)
})
input.onGesture(Gesture.TiltLeft, function () {
    mouse.movexy(-121, 0)
    basic.showLeds(`
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        `)
})
input.onGesture(Gesture.SixG, function () {
    mouse.click()
    basic.showIcon(IconNames.StickFigure)
    music.play(music.createSoundExpression(WaveShape.Sawtooth, 2987, 2882, 255, 0, 500, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
})
mouse.setStatusChangeHandler(function () {
    if (mouse.isEnabled()) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.SmallDiamond)
    }
})
keyboard.setStatusChangeHandler(function () {
    if (keyboard.isEnabled()) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.SmallDiamond)
    }
})
input.onButtonPressed(Button.B, function () {
    keyboard.sendString("w")
    basic.showLeds(`
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
        `)
})
input.onGesture(Gesture.TiltRight, function () {
    mouse.movexy(121, 0)
    basic.showLeds(`
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        `)
})
mouse.startMouseService()
keyboard.startKeyboardService()
basic.forever(function () {
	
})
