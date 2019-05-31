from microbit import *
import neopixel

uart.init(baudrate = 115200)

num_of_pixels = 24
ledring=neopixel.NeoPixel(pin0, num_of_pixels)

while True:
    msg=str(uart.read())
    if msg!="None":
        msg=msg[2:-1]
        o=msg.split(",")
        t=o[0]
        pin=int(o[1])
        r=int(o[2])
        g=int(o[3])
        b=int(o[4])
        on=o[5]
        if t=="g":
            if on=="1":
                display.set_pixel(pin%5,pin//5,9)
            else:
                display.set_pixel(pin%5,pin//5,0)
        else:
            if on=="1":
                ledring[pin]=(r,g,b)
            else:
                ledring[pin]=(0,0,0)
            ledring.show()
