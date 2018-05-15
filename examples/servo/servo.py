
'''
PWM GPIO 17  eli raspberryn pin 11
taajuus = 50 Hz
jakso = 1/ taajus = 20 ms
Funktion ChangeDutyCyle(DytyCycle) arvo 2  on kulma 0 kaytetylle servolle.
Funktion ChangeDutyCycle arvo 12 on kulma 180
DutyCycle =PulseWidth (ms)/jakso

'''
import RPi.GPIO as GPIO
import time

SERVO_PIN = 17
GPIO.setmode(GPIO.BCM) #kaytetaan GPIO portteja  
GPIO.setup(SERVO_PIN, GPIO.OUT) #asetetaan servo oupt-laitteeksi

minun_servo = GPIO.PWM(SERVO_PIN, 50) # GPIO 17  PWM 50Hz taajuudella
minun_servo.start(1) #  Alustetaan servo  jollakin arvolla
print("Kaynnistetaan servo")
try:
  	while True:
    		minun_servo.ChangeDutyCycle(2) #kulma 0 
    		time.sleep(3) #odota riittavan kaan etta servo ehtii kaantya.
    		minun_servo.ChangeDutyCycle(12) # kulma 180
    		time.sleep(3) #odota riittavan kauan, etta servo ehtii kaantya!
except KeyboardInterrupt:
  		print(" Lopetetaan..")
		minun_servo.stop()
  		GPIO.cleanup()

