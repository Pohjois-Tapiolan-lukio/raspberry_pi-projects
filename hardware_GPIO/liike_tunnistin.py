
'''****
KYTKENTA:
VCC  Pin 2 (5V)
OUT  Pin 16 (GPIO 23)
GND  Pin 6 (Ground)
***'''

import RPi.GPIO as GPIO
import time
 
SENSOR_PIN = 23
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
 
def halytys(channel):
    #  sijoita tanne komentosi!
    print("liike-tunnistin aktivoitunut")
 
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=halytys)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print("Lopetus..")
GPIO.cleanup()
