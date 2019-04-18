# IoT-apuri
IoT-apuri on kirjasto jolla saa helposti tehtyä ohjelmia jotka hyödyntävät Googlen Assistantia ääniohjaukseen, ja Shiftr.io:ta tiedonsiirtoon.

## Käyttö
Asenna MQTT-kirjasto ja googlen puhekirjastot:
```sh
sudo pip3 install paho-mqtt
sudo pip3 install SpeechRecognition
sudo pip3 install google-speech
```

### Ohjelman pohja
```python
import iot

iot.run("Raspberry", "shiftr-key", "shiftr-secret")
```

### Assistant-komento
```python
import iot

# Kuuntele sanaa "hello", ja vastaa "Hello, world!" kun käyttäjä sanoo sen
@iot.listen("hello")
def said_hello():
    iot.say("Hello, world!")

iot.run()
```

### Shiftr.io-tiedonvälitys
```python
import iot

# Luo funktio joka printtaa julkaistun viestin
@iot.subscribe("messages")
def new_message(message):
    iot.say(message)

# Julkaise (eng. publish) viesti "Hello, world!" kun käyttäjä sanoo "hello"
@iot.listen("hello")
def hello():
    iot.publish("messages", "Hello, world!")

iot.run("Raspberry", "shiftr-key", "shiftr-secret")
```


## Muuta
- Flaskista tuttuja @-merkintöjä on helppo tehdä itsekin! Linkki tutoriaaliin jossa näytetään mitä tapahtuu kirjaston puolella: https://ains.co/blog/things-which-arent-magic-flask-part-1.html
