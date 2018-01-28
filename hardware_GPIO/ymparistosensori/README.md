# Ympäristösensori
Asennus:
1. `git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
2. `cd Adafruit_Python_DHT`
3. `sudo python setup.py install`
4. Kiinnitä DHT pinniin 4 (tai muuta koodissa rivillä 15)

IoT-osio:
1. Käy vaihtamassa `iot_server_url` (annetaan tunnilla) ja `db_name` (keksi oma taulukkonimi, samat nimet ylikirjoittavat toisensa).
2. Käynnistä ohjelma, ja sitten voit käydä katsomassa kerääntyvää dataa menemällä selaimellasi osoitteeseen `<iot_server_url>/api/v1/<db_name>/print` (muista vaihtaa muuttujat samoihin mitkä ovat koodissa)
