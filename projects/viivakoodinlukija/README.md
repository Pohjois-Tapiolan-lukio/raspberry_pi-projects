# Puheohjattava viivakoodinlukija
Projektissa on kaksi puolta, palvelin- ja lukijapuoli. Palvelimella on flask-pohjainen http-palvelin, johon lukija tekee pyyntöjä. Lisäksi palvelin luo pyydettäessä sivun, jolta näkee skannatut tuotteet. Vastaavan lukijan voisi upottaa esimerkiksi älyjääkaappiin.
## Riippuvuudet
### Palvelin
* Flask `pip install flask`
* Mysql connector `pip install mysql-connector`
### Lukija
* Requests `pip install requests`
* SpeechRecognition `pip install SpeechRecognition`
* Google CloudSpeech `google-cloud-speech`

## Palvelimen valmistelu
1. Asenna sql-palvelin, esimerkiksi mariadb `apt install mariadb-server`
2. Luo tietokanta nimeltään viivakoodi `echo "CREATE DATABASE viivakoodit;"|mysql -u root -p`
3. Luo esimerkkitaulu `mysql -u root -p viivakoodit< db.sql`
