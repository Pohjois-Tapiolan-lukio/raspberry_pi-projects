
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

# Hälytyskomennot tänne! #
def halytys(channel):
    print("liike-tunnistin aktivoitunut")
    print("piip piip piip")

try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=halytys)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print("Lopetus..")
GPIO.cleanup()
