#!/usr/bin/python3
import iot

# Kuuntele sanaa "hello", ja vastaa "Hello, world!" kun käyttäjä sanoo sen
@iot.listen("hello")
def said_hello():
    iot.say("Hello. ")
    
@iot.listen("forward")
def said_forward():
    iot.publish("messages","forward")
    iot.say("Asking the car to move forward")

@iot.listen("back")
def said_back():
    iot.publish("messages","back")
    iot.say("Asking the car to move backward")
    
@iot.listen("left")
def said_left():
    iot.publish("messages","left")
    iot.say("Asking the car to move left")
    
@iot.listen("right")
def said_right():
    iot.publish("messages","right")
    iot.say("Asking the car to move right")

@iot.listen("green")
def said_green():
    iot.publish("messages","green")

@iot.listen("red")
def said_red():
    iot.publish("messages","red")
    
@iot.listen("animation")
def said_animation():
    iot.publish("messages","animation")

@iot.listen("no light")
def said_nolight():
    iot.publish("messages","nolight")

@iot.listen("How are you")
def said_How_are_you():
    iot.say("I'm good. Thank you for asking ")
    
'''@iot.listen("Tell me a joke")
def said_Tell_me_a_joke():
    iot.say("What is red and bad for your teeth?,, a brick. hehehe ")
'''
iot.run("voice1","shiftr-key","shiftr-secret")
