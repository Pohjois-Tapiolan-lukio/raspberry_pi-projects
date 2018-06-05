import iot

# Kuuntele sanaa "hello", ja vastaa "Hello, world!" kun käyttäjä sanoo sen
@iot.listen("hello")
def said_hello():
    iot.say("Hello, world!")

iot.run()
