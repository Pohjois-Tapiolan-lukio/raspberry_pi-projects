'''
kaytossa GPIO portit 17, 27, 23, 24 , arduinon moottorinohjauskorttissa l293d.
suorita ensin: python l293d.py

'''

import RPi.GPIO as GPIO
import time
from l293d import L293D
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
motor = L293D(17,27,23,24)
motor.stop()
 
for i in range(20):
  motor.forward()
  time.sleep(0.5)
  motor.forwardRight()
  time.sleep(0.5)
motor.stop()

