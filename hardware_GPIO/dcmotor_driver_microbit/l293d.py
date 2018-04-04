
import RPi.GPIO as GPIO
import time
import threading
 
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
 
class L293D():
    DIST_PER_SEC  = 35.0 # cm/s
    SEC_PER_TURN  = 2.087 # seconds per full turn (depending on the base material, use forwardLeft(), stop() and time.time() to measure the time)
 
    def __init__(self, left_pin1, left_pin2, right_pin1, right_pin2):
        self.MOTOR_LEFT_PIN1  = left_pin1
        self.MOTOR_LEFT_PIN2  = left_pin2
        self.MOTOR_RIGHT_PIN1 = right_pin1
        self.MOTOR_RIGHT_PIN2 = right_pin2
 
        GPIO.setup(self.MOTOR_LEFT_PIN1, GPIO.OUT)
        GPIO.setup(self.MOTOR_LEFT_PIN2, GPIO.OUT)
        GPIO.setup(self.MOTOR_RIGHT_PIN1, GPIO.OUT)
        GPIO.setup(self.MOTOR_RIGHT_PIN2, GPIO.OUT)
 
    def forwardLeft(self):
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
        return time.time()
 
    def forwardRight(self):
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.HIGH)
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        return time.time()
 
    def forward(self):
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.HIGH)
        return time.time()
 
    def backwardLeft(self):
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.HIGH)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        return time.time()
 
    def backwardRight(self):
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        return time.time()
 
    def backward(self):
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.HIGH)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
        return time.time()
 
    def stop(self):
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
 
    def forwardDistance(self, dist):
        self.forward()
        threading.Timer(dist/self.DIST_PER_SEC, self.stop)
 
    def backwardDistance(self, dist):
        self.backward()
        threading.Timer(dist/self.DIST_PER_SEC, self.stop)



