from microbit import *
import radio
import music
radio.on()
radio.config(channel = 83)
while True:
    if button_a.was_pressed():
        radio.send(str("Awaiting Response"))
        music.play(music.POWER_UP)
        incoming = radio.receive()
        if incoming:
            if incoming == "Ready for battle":
                display.scroll(incoming)
                if button_b.was_pressed():
                    radio.send(str("Fight !"))
                    music.play(music.POWER_DOWN)