import RPi.GPIO as GPIO
import time
from l293d_pwm import L293DPWM
import threading 
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
car = L293DPWM(24, 12, 26, 13, 5, 6)
car.stop()


car.forward(100,100)
print("forward")
time.sleep(2)
car.stop()
car.backward(100,100)
print("reverse")
time.sleep(2)
car.stop()
car.forward(50,100)
print("left")
time.sleep(2)
car.forward(100, 50)
print("right")
time.sleep(2)

car.stop()
