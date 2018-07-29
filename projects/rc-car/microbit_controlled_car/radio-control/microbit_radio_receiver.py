# Add your Python code here. E.g.
from microbit import *

import radio

radio.on()
radio.config(channel = 50)


timeout_counter = 0

while True:
    message = radio.receive()
    
    if message != None:
        print(message)
        timeout_counter = 0
    
    elif timeout_counter == 100:
        print('0.0  0.0')
    
    else:
        timeout_counter += 1 
    
    sleep(20)