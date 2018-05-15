from microbit import *
import radio
radio.on()  # Radio paalle
radio.config(channel=50)  # valitse kanava valilta 0 -100
while True:
    display.clear()
    gesture = accelerometer.current_gesture()
    if button_a.is_pressed:
        display.show("<")
        radio.send("vasemmalle")
    elif button_a.is_pressed:
        display.show(">")
        radio.send("oikealle")
    elif gesture == "face up":
        display.show("^")
        radio.send("eteenpain")
    else:
        display.show("-")
    sleep(100)
