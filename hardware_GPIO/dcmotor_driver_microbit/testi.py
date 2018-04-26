'''
kaytossa GPIO portit 17, 27, 23, 24 , arduinon moottorinohjauskorttissa l293d.
suorita ensin: python l293d.py

'''

from gpiozero import Button #kayttaa Broadcomin (BMC) pinninumerointia
import RPi.GPIO as GPIO
from l293d import L293D

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print("Keskeytä Ctrl+C")
#Microbit kytketaan raspberryn GPIO4:seen eli fysikaalinen pinni 7
ohjain_eteenpain = Button(4, pull_up = False)
#Microbit kytketaan raspberryn GPIO5:seen eli fysikaalinen pinni 8
ohjain_oikealle = Button(5, pull_up = False)
#Microbit kytketaan raspberryn GPIO6:seen eli fysikaalinen pinni 9
ohjain_vasemmalle = Button(6, pull_up = False)

motor = L293D(17,27,23,24)
motor.stop()

try:
  while True:
    if ohjain_eteenpain.is_pressed:
      motor.forward()
    if ohjain_oikealle.is_pressed:
      motor.forwardRight()
    if ohjain_vasemmalle.is_pressed:
      motor.forwardLeft()
except KeyboardInterrupt:
  print("Lopetetaan ohjelma")
finally:
  motor.stop()
