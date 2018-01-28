'''
Esimerkissa lahetaan arduinosta analogisen sensorin arvo raspberryn usb-porttiin. Loydat oikean kanavan usb-laitteelle seuraavasti.
1) Anna komento ls -l /dev/tty*
2) Kytke arduino raspberryn usb-porttiin.
3) Anna komento ls -l /dev/tty* uudestaan, ja etsi ero laitelistauksissa.
Yleensa /dev/ttyACM0 !!
'''
import serial
import time

ser = serial.Serial('/dev/ttyACM2',9600)


try:
	while True:
		#Vastaanotetaan arduinon viesti
		input_read_serial = ser.readline()
		print(input_read_serial)

		time.sleep(0.01)

except KeyboardInterrupt:
		#ohjelman keskeytys
		print(" Ohjelman suoritus paattyy")
