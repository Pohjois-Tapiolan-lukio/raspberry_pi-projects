'''
Kaytetaan fysikaalista pinnia  12  (gpio 18)
DutyCycle eli pulssisuhde :    0.0 <= pulssisuhde <= 100.0
Kytke led +napa raspberryn porttiin 12 ja -napa porttiin GND (pinni 3)
'''



import time
import RPi.GPIO as GPIO

LED_PIN = 12

GPIO.setmode(GPIO.BOARD)#kaytetaan fyysista pinnia 12
GPIO.setup(LED_PIN, GPIO.OUT)


led = GPIO.PWM(LED_PIN, 50)  # fysiinen pinni =12, taajuus 50 Hz
led.start(0)
try:
    print(" Ctrl + C lopettaa ohjelman")
    while True:
        for pulssisuhde in range(0, 101, 5):
            led.ChangeDutyCycle(pulssisuhde)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            led.ChangeDutyCycle(pulssisuhde)
            time.sleep(0.1)
except KeyboardInterrupt:
    print(" Lopetetaan ohjelma.")
led.stop()
GPIO.cleanup()
