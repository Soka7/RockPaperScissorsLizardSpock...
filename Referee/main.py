from microbit import *
import radio
import music
from StackFile import Stack

radio.on()
radio.config(channel = 83)

PlayerNum = 0

Memory1 = Stack()
Memory2 = Stack()

dico = {}

while True:
    incoming = radio.receive()
    if incoming:
        if incoming[:4] == "Ping":
            display.scroll(incoming)
            PlayerNum += 1
            if Memory1 not in dico.values():
                dico[incoming[-4:]] = Memory1
                Ping1 = incoming[-4:]
            else:
                dico[incoming[-4:]] = Memory2
                Ping2 = incoming[-4:]
            incoming = None
    if PlayerNum == 2:
        while True:
            if button_b.is_pressed():
                radio.send(str("Fight !"))
                display.scroll("Fight !")
                music.play(music.POWER_DOWN)
                break
        while True:
            incoming = radio.receive()
            if incoming:
                if incoming != None:
                    display.scroll(str("ok"))
                    if type(incoming[:4]) != None:
                        incoming = incoming[8:]
                        display.scroll(str("ok"))
                        display.scroll(incoming[:5])
                        display.scroll(incoming[-4:])
                        if incoming[-4:] == Ping1:
                            display.scroll(incoming)
                            display.scroll(incoming[:5])
                            dico[incoming[-4:]].ToStack(incoming[:5])
                            display.scroll(str(Memory1._stack))
                        elif incoming[-4:] == Ping2:
                            display.scroll(incoming)
                            display.scroll(incoming[:5])
                            dico[incoming[-4:]].ToStack(incoming[:5])
                            display.scroll(str(Memory2._stack))