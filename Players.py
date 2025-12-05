from microbit import *
import radio
from GameData import Actions
from GameData import Matching
import music

class JoueurC:
    def __init__(self, nom, num = None):
        self.nom = nom
        self.num = num

    def GetCall(self):
        while True:
            if button_a.is_pressed(): # Used to send the message to the server
                display.scroll(str("Ready"))
                radio.send(str("Ready"))
                music.play(music.POWER_UP) 
                break

    def Play(self):
        compteur = 0
        while True:
            if button_a.was_pressed(): # Switch the action to another and allow it to loop using modulo
                compteur = (compteur + 1) % 5 #Thx to Yolked.
                display.show(Actions[Matching[compteur]]["Shape"])
                sleep((2000))
            elif button_b.was_pressed(): # Break out the loop because the action was selected
                display.clear()
                break
        ToSend = str(Matching[compteur]) # Prepare the message to send and send it to the server
        radio.send(ToSend + str(self.num))
        display.scroll(str(ToSend + str(self.num)))
