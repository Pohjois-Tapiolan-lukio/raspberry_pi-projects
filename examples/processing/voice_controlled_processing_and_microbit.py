#!/usr/bin/python3
import iot
import serial

ser = serial.Serial('/dev/ttyACM0', baudrate= 115200, timeout=1)

# Kuuntele sanaa "hello", ja vastaa "Hello, world!" 
@iot.listen("red ring")
def print_red():
    print('0\n')
    ser.write(b'0\n')

@iot.listen("no ring")
def print_green():
    print('no ring')
    ser.write(b's')
    iot.publish("messages", "s")

@iot.listen("blue ring")
def print_one():
    print('blue ring')
    ser.write(b'k')
    iot.publish("messages", "k")
@iot.listen("lights on")
def said_hello():
    iot.say("Hi there, I am shining.")
    #iot.publish("messages","blue")
    
@iot.listen("sparkle")
def said_forward():
    iot.publish("messages","sparkle")
    iot.say("OK, sparkle")

@iot.listen("green star")
def said_back():
    iot.publish("messages","green")
    #iot.say("Asking the car to move backward")
    
@iot.listen("blue star")
def said_left():
    iot.publish("messages","blue")
    
@iot.listen("red star")
def said_left():
    iot.publish("messages","red")
    

@iot.listen("green glitter")
def said_back():
    iot.publish("messages","green glitter")

@iot.listen("red glitter")
def said_back():
    iot.publish("messages","red glitter")

@iot.listen("blue glitter")
def said_back():
    iot.publish("messages","green glitter")

@iot.listen("rainbow")
def said_back():
    iot.publish("messages","rainbow")
    
    
@iot.listen("no light")
def said_right():
    iot.publish("messages","nolight")
    #iot.say("Asking the car to move right")


@iot.listen("no light")
def said_nolight():
    iot.publish("messages","nolight")

@iot.listen("How are you")
def said_How_are_you():
    iot.say("I'm good. Thank you for asking ")

iot.run("voice1","shiftr-key","shiftr-secret")
 