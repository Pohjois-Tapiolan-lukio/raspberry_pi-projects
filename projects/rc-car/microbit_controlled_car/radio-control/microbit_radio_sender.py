# Add your Python code here. E.g.
from microbit import *
from math import *
import radio

radio.on()
radio.config(channel = 50)

acc = accelerometer
payload = ""

while True:
    
    vec = (acc.get_x(), acc.get_y(), acc.get_z())
    pitch = atan2(vec[1], vec[2])
    roll = atan2(vec[0], vec[2])
    
    new_payload = "{:10.2f} {:10.2f}".format(cos(roll)*degrees(pitch),
        cos(pitch)*degrees(roll))
    

    if payload != new_payload:
        radio.send(new_payload)
    
    payload = new_payload
    sleep(20)