from microbit import *
import neopixel

uart.init(baudrate = 115200)

num_of_pixels = 24
ledring = neopixel.NeoPixel(pin0, num_of_pixels)


def lights(red, green, blue):
    global ledring
    for i in range(24):
        ledring[i] = (red, green, blue)  # RGB -values
        sleep(50)
        ledring.show()

while True:
    message_bytes = uart.read()
    message = str(message_bytes)
    if "k" in message:
        uart.write(b'Lights ON')
        lights(0, 0, 255)
    elif "s" in message:
        uart.write(b'Lights OFF')
        lights(0, 0, 0)
    