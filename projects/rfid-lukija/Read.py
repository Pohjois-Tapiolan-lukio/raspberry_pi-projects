import RPi.GPIO as GPIO
import SimpleMFRC522
import time

reader = SimpleMFRC522.SimpleMFRC522()

SERVO_PIN = 17
GPIO.setmode(GPIO.BCM) #kaytetaan GPIO portteja  
GPIO.setup(SERVO_PIN, GPIO.OUT) #asetetaan servo oupt-laitteeksi

GPIO.setup(23, GPIO.OUT)
piezo = GPIO.PWM(23, 100)

minun_servo = GPIO.PWM(SERVO_PIN, 50) # GPIO 17  PWM 50Hz taajuudella
minun_servo.start(1) #  Alustetaan servo  jollakin arvolla
minun_servo.ChangeDutyCycle(12) #kulma 0 
print("Kaynnistetaan servo")

try:
        while True:
                id, text = reader.read()
                print(id)
                print(text)              
                if id == 441692598382: #Kortin numero
                        minun_servo.ChangeDutyCycle(3) #kulma 0 
                        time.sleep(3) #odota riittavan kaan etta servo ehtii kaantya.
                        minun_servo.ChangeDutyCycle(12) # kulma 180
                        time.sleep(3) #odota riittavan kauan, etta servo ehtii kaantya!
                        id = 0
                else:
                        for i in range(0,3):
                                print("Piip")
                                GPIO.output(23, True)
                                piezo.start(100)
                                piezo.ChangeFrequency(440)
                                time.sleep(0.5)
                                piezo.stop()
                                time.sleep(0.2)
except KeyboardInterrupt:
                print(" Lopetetaan..")
                minun_servo.stop()
                GPIO.cleanup()
