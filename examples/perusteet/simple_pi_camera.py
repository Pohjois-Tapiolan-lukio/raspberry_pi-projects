#tuodaan kirjastoja käyttöön
from picamera import PiCamera 
from time import sleep

# Luodaan camera-niminen ilmentymä eli olio PiCamera() funktiolla
camera=PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Documents/mxheikki/image1.jpg') # nyt otetaan valokuva
camera.stop_preview()
