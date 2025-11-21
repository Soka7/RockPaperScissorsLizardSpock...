from microbit import *
import radio
import music
radio.on()
radio.config(channel = 83)
while True:
    Ready = 0
    if button_a.was_pressed():
        radio.send(str("Awaiting Response J1"))
        music.play(music.POWER_UP)
        incoming = radio.receive()
        if incoming and incoming == "Ready for battle J1":
            Ready += 1
    if button_a.was_pressed():
        radio.send(str("Awaiting Response J2"))
        music.play(music.POWER_UP)
        incoming = radio.receive()
        if incoming and incoming == "Ready for battle J2":
            Ready += 1

    if Ready == 2:
        display.scroll(incoming)
        if button_b.was_pressed():
            radio.send(str("Fight !"))
            music.play(music.POWER_DOWN)