'''
asennus:
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install

Kaytossa DHT11 tai DHT22
Anna GPIO NRO (koodisa 4)  
'''
import Adafruit_DHT
import time
import sys

sensor = Adafruit_DHT.DHT22
pin = 4

def mittaus():
	kosteus, lampotila = Adafruit_DHT.read_retry(sensor, pin)
	return kosteus, lampotila 

if __name__ == '__main__':
	try:
		while True:
			mitattu_kosteus, mitattu_lampotila = mittaus()
			if mitattu_kosteus is not None and mitattu_lampotila is not Note:
				print("Kosteus {0:.1f} ja lampotila {1:.1.f}".format(mitattu_kosteus, mitattu_lampotila))
			else:
				print("Mittaus ei onnistunut!")
			time.sleep(1)
	except KeyboardInterrupt:
		print("lopetetaan mittaus!")
		
