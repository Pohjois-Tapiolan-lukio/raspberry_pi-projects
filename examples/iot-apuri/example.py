import time
import iot

# Valmistele iot-kirjasto
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
