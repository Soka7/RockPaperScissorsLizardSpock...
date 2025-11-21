from microbit import *
from Joueurs import JoueurC
import radio
radio.on()
radio.config(channel = 83)

Joueur1 = JoueurC("Joueur1", "Awaiting Reponse J1", 1)

while True:
    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)
        if incoming == Joueur1.Await:
            Joueur1.GetCall()
        elif incoming == "Fight !":
            Joueur1.Play()
        sleep(2000)
    display.clear()