#Yhdista microbit pin1 raspberryn Gpio 4:een eli fysikaalinen pinni 7.
from microbit import *
import radio
radio.on()  # Radio paalle
radio.config(channel=50)  # valitse kanava valilta 0 -100
while True:
    display.clear()
    viesti = radio.receive()  # haetaan radioviestia
    
    if viesti == "laukaise":
        display.scroll("KUVA!")
        display.show(Image.SQUARE)
        sleep(250)
        display.show(Image.SQUARE_SMALL)
        sleep(250)  # Odota 0.5 sekunttia
        pin1.write_digital(1)
        sleep(3000)
        pin1.write_digital(0)