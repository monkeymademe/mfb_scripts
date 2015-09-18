import pibrella, signal


def button_changed(pin):
    if pin.read() == 1:
	pibrella.output.e.on()
    else:
        pibrella.output.e.off()

pibrella.button.changed(button_changed)

signal.pause()     
