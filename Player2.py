from microbit import *
from Joueurs import JoueurC
import radio
radio.on()
radio.config(channel = 83)

Joueur2 = JoueurC("Joueur2", "Awaiting Reponse J2", 2)

while True:
    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)
        if incoming == Joueur2.Await:
            Joueur2.GetCall()
        elif incoming == "Fight !":
            Joueur2.Play()
        sleep(2000)
    display.clear()