from picamera import PiCamera
from gpiozero import Button #kayttaa Broadcomin (BMC) pinninumerointia
from time import sleep

print("Keskeytä Ctrl+C")
#Microbit kytketaan raspberryn GPIO4:seen eli fysikaalinen pinni 7
laukaisin = Button(4, pull_up = False)

#Luodaan oma kamera kayttoon.
camera = PiCamera()
camera.resolution = (1024, 768) # aseta kuvan resoluutio
camera.vflip = True #  kuvan kaanto, vflip=vertical flip, hflip= horizontal.. 
try:
        camera.start_preview()
        sleep(3)
        laukaisin.wait_for_press() # odota kunnes laukausuviesti saapuu..
        camera.capture('kuva.jpg')
        camera.stop_preview()
        camera.close()

except KeyboardInterrupt:
    print("Lopetetaan ohjelma")
