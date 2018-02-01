'''

Kayttojannite 3.3V PIN1
GND PIN6

Nappi output pin 11  GPIO17
Led-lamppu pin 13 eli GPIO27
'''
import time
import RPi.GPIO as GPIO

NAPPI_GPIO = 17 #  valitaan napille kaytettava portti
LED_GPIO = 27 # valitaan  ledille portti
GPIO.setmode(GPIO.BCM) # Tassa  asetetaan kayttoon GPIO numero.
GPIO.setup(NAPPI_GPIO, GPIO.IN) # Asetetaan Nappi INPUT
#GPIO.setmode(GPIO.BOARD) Jos kaytat fyysista pinnia 12
GPIO.setup(LED_GPIO, GPIO.OUT) #Asetetaan led OUTPUT tilaan
 

print("testataan napintoimintaa")

try:
        while True:
		if  GPIO.input(NAPPI_GPIO):
                	GPIO.output(LED_GPIO, GPIO.HIGH) # sytytetaan led
                	print("Led ON")
                else:
                	GPIO.output(LED_GPIO, GPIO.LOW) # kaynnistetan rele.
                	print("led off")
                #time.sleep(1)

except KeyboardInterrupt:
        print(" Lopetus..")
        GPIO.cleanup()


