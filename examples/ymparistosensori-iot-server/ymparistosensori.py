'''
Asennusohjeet:
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install

Kaytossa DHT11 tai DHT22
Anna GPIO NRO (koodisa 4)
'''
import Adafruit_DHT
import time
import sys
import requests

sensor = Adafruit_DHT.DHT22
pin = 4
iot_server_url = "http://192.168.43.158:5000"
db_name = "ymparistosensori-0000"


def laheta_data(url_loppu):
        # Lähetetään GET-request IoT-serverille osoitteeseen esim.:
        # http://192.168.43.158:5000/api/v1/create/kosteus;lampotila

        return requests.get("{:s}/api/v1/{:s}/{:s}".format(iot_server_url, db_name, url_loppu))

def mittaus():
        kosteus, lampotila = Adafruit_DHT.read_retry(sensor, pin)
        return kosteus, lampotila

if __name__ == '__main__':
        try:
                laheta_data("create/kosteus;lampotila")
                while True:
                        mitattu_kosteus, mitattu_lampotila = mittaus()
                        if mitattu_kosteus is not None and mitattu_lampotila is not Note:
                                print("Kosteus {0:.1f} ja lampotila {1:.1.f}".format(mitattu_kosteus, mitattu_lampotila))
                                laheta_data("insert/{:s};{:s}".format(mitattu_kosteus, mitattu_lampotila))
                        else:
                                print("Mittaus ei onnistunut!")
                        time.sleep(1)
        except KeyboardInterrupt:
                print("Lopetetaan mittaus!")
