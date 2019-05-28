#ping_pong in microbit
from microbit import *
uart.init(baudrate = 115200)

sleep(5000)
uart.write(b'ping')

while True:
    message_bytes = uart.read()
    message = str(message_bytes)
    if  "pong" in message:
        uart.write(b'ping')
    sleep(500)