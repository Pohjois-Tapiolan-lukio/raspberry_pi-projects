# Add your Python code here. E.g.
from microbit import *

import radio

radio.on()
radio.config(channel = 50)



while True:
    message = radio.receive()
    
    if message != None:
        print(message)
    
    sleep(20)