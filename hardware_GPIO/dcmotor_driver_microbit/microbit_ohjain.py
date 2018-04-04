from microbit import *
import radio
radio.on()  # Radio paalle
radio.config(channel=50)  # valitse kanava valilta 0 -100
while True:
    display.clear()
    viesti = radio.receive()  # haetaan radioviestia

    if viesti != None:
        display.show("!");
        pin0.write_digital(0);
        pin1.write_digital(0);
        pin2.write_digital(0);
        if viesti == "eteenpain":
            pin0.write_digital(1)
        elif viesti == "vasemmalle":
            pin1.write_digital(1)
        elif viesti == "oikealle":
            pin2.write_digital(1)
    else:
        display.show(".");
