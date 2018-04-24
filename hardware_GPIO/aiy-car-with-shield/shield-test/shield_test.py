import RPi.GPIO as GPIO
import time
from l293d import L293D
import threading 
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
car = L293D(24,12,13,5)
car.stop()


PIN_LEFT = 26
PIN_RIGHT = 6

GPIO.setup(PIN_LEFT, GPIO.OUT)
GPIO.setup(PIN_RIGHT, GPIO.OUT)


PWM_MOTOR_LEFT = GPIO.PWM(PIN_LEFT, 50)
PWM_MOTOR_RIGHT = GPIO.PWM(PIN_RIGHT, 50)

PWM_MOTOR_LEFT.start(1)
PWM_MOTOR_RIGHT.start(1)

car.forward()
PWM_MOTOR_LEFT.ChangeDutyCycle(100)
PWM_MOTOR_RIGHT.ChangeDutyCycle(100)
time.sleep(2)
PWM_MOTOR_LEFT.ChangeDutyCycle(50)
PWM_MOTOR_RIGHT.ChangeDutyCycle(50)
time.sleep(2)
car.stop()
