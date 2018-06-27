# Puheohjattava viivakoodinlukija
Projektissa on kaksi puolta, palvelin- ja lukijapuoli. Palvelimella on flask-pohjainen http-palvelin, johon lukija tekee pyyntöjä. Lisäksi palvelin luo pyydettäessä sivun, jolta näkee skannatut tuotteet.
## Riippuvuudet
### Palvelin
* Flask `pip install flask`
* Mysql connector `pip install mysql-connector`
### Lukija
* Requests `pip install requests`
* SpeechRecognition `pip install SpeechRecognition`
* Google CloudSpeech `google-cloud-speech`
