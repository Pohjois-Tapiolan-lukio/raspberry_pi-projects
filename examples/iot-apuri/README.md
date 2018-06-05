# IoT-apuri
IoT-apuri on kirjasto jolla saa helposti tehtyä ohjelmia jotka hyödyntävät Googlen Assistantia ääniohjaukseen, ja Shiftr.io:ta tiedonsiirtoon.

## Käyttö
Asenna MQTT-kirjasto:
```sh
sudo pip3 install paho-mqtt
```

### Ohjelman pohja
```python
import iot

# Valmistele iot-kirjasto
iot.setup("Raspberry", "shiftr-key", "shiftr-secret")
```

### Assistant-komento
```python
import iot

# Valmistele iot-kirjasto
iot.setup()

# Kuunnellaan sanaa "hello", ja vastataan "Hello, world!" kun käyttäjä sanoo sen
@iot.listen("hello")
def said_hello():
    iot.say("Hello, world!")
```

### Shiftr.io-tiedonvälitys
```python
import time
import iot

# Valmistele iot-kirjasto (parametreinä shiftr-tiedot)
iot.setup("Raspberry", "shiftr-key", "shiftr-secret")

# Luo funktio joka printtaa julkaistun viestin
@iot.subscribe("messages")
def new_message(message):
    print(message)

# Julkaise (eng. publish) viesti "Hello, world!"
iot.publish("messages", "Hello, world!")

# Anna shiftr.io:lle aikaa saada julkaistu viesti ja lähettää se takaisin
# (jotta new_message-funktio voi printata sen)
time.sleep(2)
```


## Muuta
- Flaskista tuttuja @-merkintöjä on helppo tehdä itsekin! Linkki tutoriaaliin jossa näytetään mitä tapahtuu kirjaston puolella: https://ains.co/blog/things-which-arent-magic-flask-part-1.html
