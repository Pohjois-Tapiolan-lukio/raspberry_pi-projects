from microbit import *
from math import *

acc = accelerometer

while True:
    vec = (acc.get_x(), acc.get_y(), acc.get_z())
    pitch = atan2(vec[1], vec[2])
    roll = atan2(vec[0], vec[2])
    
    print("{:10.2f} {:10.2f}".format(cos(roll)*degrees(pitch),
        cos(pitch)*degrees(roll)))
    
    sleep(20)