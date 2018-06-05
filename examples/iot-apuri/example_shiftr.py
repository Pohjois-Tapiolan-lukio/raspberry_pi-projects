import time
import iot

# Luo funktio joka printtaa julkaistun viestin
@iot.subscribe("messages")
def new_message(message):
    iot.say(message)

# Julkaise (eng. publish) viesti "Hello, world!" kun käyttäjä sanoo "hello"
@iot.listen("hello")
def hello():
    iot.publish("messages", "Hello, world!")

# Anna shiftr.io:lle aikaa saada julkaistu viesti ja lähettää se takaisin
# (jotta new_message-funktio voi printata sen)
time.sleep(2)

iot.run("Raspberry", "shiftr-key", "shiftr-secret")
