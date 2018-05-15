# Lahettaa viestin raspberryyn yhdistettyyn microbittiin kuvan ottoa varten.
from microbit import *
import radio

radio.on()  # radio paalle.
radio.config(channel=50)  # Valitse sama kanava lahettimeen ja vastaanottimeen.

while True:
    display.show(Image.HAPPY)
    if button_a.was_pressed():
        radio.send("laukaise")
        display.show(Image.DIAMOND)
        sleep(250)
        display.show(Image.DIAMOND_SMALL)
        sleep(250)
        display.clear()
    sleep(50)