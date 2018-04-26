import RPi.GPIO as GPIO
import time
from l293d_pwm import L293DPWM
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
car = L293DPWM(24, 12, 26, 13, 5, 6)
car.stop()


car.forward(90, 100)
print("forward")
time.sleep(2)
car.stop()
car.backward(90, 100)
print("reverse")
time.sleep(2)
car.stop()
car.forward(25*0.9, 100)
print("left")
time.sleep(2)
car.forward(90, 90*0.25)
print("right")
time.sleep(2)
car.stop()
