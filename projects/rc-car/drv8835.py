import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class DRV8835():
    def __init__(self):
        self.LEFT = 12
        self.RIGHT = 13
        
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)

        GPIO.setup(self.LEFT, GPIO.OUT)
        GPIO.setup(self.RIGHT, GPIO.OUT)
        
        self.LEFT_PWM = GPIO.PWM(5)
        self.LEFT_PWM.start(1)
        self.RIGHT_PWM = GPIO.PWM(6)
        self.RIGHT_PWM.start(1)

    def forward(self, left_speed, right_speed):
        self.set_motor_speed(self.LEFT_PWM, self.LEFT, left_speed)
        self.set_motor_speed(self.RIGHT_PWM, self.RIGHT, right_speed)

    def backward(self, left_speed, right_speed):
        self.set_motor_speed(self.LEFT_PWM, self.LEFT, -left_speed)
        self.set_motor_speed(self.RIGHT_PWM, self.RIGHT, -right_speed)

    def set_motor_speed(self, motor, dir_pin, speed):
        if speed < 0:
            GPIO.output(dir_pin, GPIO.HIGH)
            speed = -speed
        else:
            GPIO.output(dir_pin, GPIO.LOW)
        motor.ChangeDutyCycle(speed)

    def stop(self):
        self.set_motor_speed(self.LEFT_PWM, self.LEFT, 0)
        self.set_motor_speed(self.RIGHT_PWM, self.RIGHT, 0)
