import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class L293DPWM():
    DIST_PER_SEC  = 35.0 # cm/s default 35
    SEC_PER_TURN  = 2.087 # seconds per full turn (depending on the base material, use forwardLeft(), stop() and time.time() to measure the time)

    def __init__(self, left_pin1, left_pin2, left_pwm, right_pin1, right_pin2, right_pwm):
        self.MOTOR_LEFT_PIN1  = left_pin1
        self.MOTOR_LEFT_PIN2  = left_pin2
        self.MOTOR_RIGHT_PIN1 = right_pin1
        self.MOTOR_RIGHT_PIN2 = right_pin2

        GPIO.setup(self.MOTOR_LEFT_PIN1, GPIO.OUT)
        GPIO.setup(self.MOTOR_LEFT_PIN2, GPIO.OUT)
        GPIO.setup(left_pwm, GPIO.OUT)
        GPIO.setup(self.MOTOR_RIGHT_PIN1, GPIO.OUT)
        GPIO.setup(self.MOTOR_RIGHT_PIN2, GPIO.OUT)
        GPIO.setup(right_pwm, GPIO.OUT)

        self.MOTOR_LEFT_PWM = GPIO.PWM(left_pwm, 50)
        self.MOTOR_RIGHT_PWM = GPIO.PWM(right_pwm, 50)

        self.MOTOR_LEFT_PWM.start(1)
        self.MOTOR_RIGHT_PWM.start(1)

    def forward(self, left_speed, right_speed):
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.HIGH)
        self.MOTOR_LEFT_PWM.ChangeDutyCycle(left_speed)
        self.MOTOR_RIGHT_PWM.ChangeDutyCycle(right_speed)
        return time.time()

    def backward(self, left_speed, right_speed):
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.HIGH)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.HIGH)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
        self.MOTOR_LEFT_PWM.ChangeDutyCycle(left_speed)
        self.MOTOR_RIGHT_PWM.ChangeDutyCycle(right_speed)
        return time.time()

    def stop(self):
        GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
        GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
        self.MOTOR_LEFT_PWM.ChangeDutyCycle(0)
        self.MOTOR_RIGHT_PWM.ChangeDutyCycle(0)

    def forwardDistance(self, dist):
        self.forward()
        threading.Timer(dist/self.DIST_PER_SEC, self.stop)

    def backwardDistance(self, dist):
        self.backward()
        threading.Timer(dist/self.DIST_PER_SEC, self.stop)
