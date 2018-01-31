'''
Releella ohjataan virtapiirin toimintaa. 
Releen ohjausignaali PIN11 eli GPIO 17
Kayttojannite 3.3V PIN1
GND PIN6
Jos kaytat 5V jannitetta, niin kytke  1 kohm vastus input pinnin
ja gpio.
Releen ulostulossa  avaataan keskimmaisen-ja -reunaportin valinen portti.
'''
import time
import RPi.GPIO as GPIO

RELE_GPIO = 17 #  valitaan kaytettava portti
GPIO.setmode(GPIO.BCM) # Tassa  asetetaan kayttoon GPIO numero.
GPIO.setup(RELE_GPIO, GPIO.OUT) # Asettaan GPIO  OUTPUT-tilaan.
 

try:
	while True:
		GPIO.output(RELE_GPIO, GPIO.LOW) # suljetaaan rele.
		print("suljetaan rele")
		time.sleep(1)
		GPIO.output(RELE_GPIO, GPIO.HIGH) # kaynnistetan rele.
		print("avataan rele.")
		time.sleep(1)

except KeyboardInterrupt:
    	print(" Lopetus..")
	GPIO.cleanup()
