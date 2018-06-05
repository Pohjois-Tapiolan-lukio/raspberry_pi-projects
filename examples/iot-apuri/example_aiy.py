import iot

# Valmistele iot-kirjasto
iot.setup()

# Kuunnellaan sanaa "hello", ja vastataan "Hello, world!" kun käyttäjä sanoo sen
@iot.listen("hello")
def said_hello():
    iot.say("Hello, world!")
