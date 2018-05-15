'''
Esimerkissa lahetaan arduinosta analogisen sensorin arvo raspberryn usb-porttiin. Loydat oikean kanavan usb-laitteelle seuraavasti.
1) Anna komento ls -l /dev/tty*
2) Kytke arduino raspberryn usb-porttiin.
3) Anna komento ls -l /dev/tty* uudestaan, ja etsi ero laitelistauksissa.
Yleensa /dev/ttyACM0 !!
'''
import serial
import time

ser = serial.Serial("/dev/ttyACM0", 9600)

try:
    
    while True:
        # Vastaanotetaan arduinon viesti
        serial_in = ser.readline()
        print(serial_in)
        print("Found message:", serial_in)
        if "ping" in str(serial_in):
            # Kun saadaan viesti jossa on "ping", lahetetaan "pong"
            ser.write(b"pong")
        time.sleep(0.5)
except KeyboardInterrupt:
    # Ohjelman keskeytys
    ser.close()
    print("Ohjelman suoritus paattyy")
