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
