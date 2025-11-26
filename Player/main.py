from microbit import *
import radio
from players import *

radio.on()
radio.config(channel = 83)

while True:
    incoming = radio.receive()
    if incoming:
        display.scroll(bruh1.duh)
        if incoming == "Awaiting Response":
            continue
        else:
            continue
    display.clear()
