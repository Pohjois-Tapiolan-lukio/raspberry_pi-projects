#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# dbws_trafficlight.py
# Voice Controlled Traffic Light
# Modified by DroneBot Workshop
# 2018-02-20
# Modified by Matti Heikkinen
# 2018-04-20
#

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

The Google Assistant Library can be installed with:
    env/bin/pip install google-assistant-library==0.0.2

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import subprocess
import sys
#from time import sleep
import time
#import threading
from random import randint
import aiy.assistant.auth_helpers
import aiy.audio
import aiy.voicehat
from google.assistant.library import Assistant
from google.assistant.library.event import EventType

import paho.mqtt.client as mqtt
client = mqtt.Client(client_id = "<your device name>")
client.username_pw_set("<Username>", password = "<your password>")
client.connect("broker.shiftr.io", 1883, 60)
client.loop_start()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import serial
ser = serial.Serial("/dev/ttyACM0", 9600)




logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

#MQTT connect to shiftr.io
def send_message(client, command):
    print("Auton kommennot: j = vasemmalle, i=eteenpain, k=stop,  l=oikealle ja m=taakse\n")
    print("Lednauhan ohjaus: red, green, blue, white, nolight, rainbow\n")
    #command = input("anna auton tai lednauhan ohjauskomento: j, i, k, l, m\n")
    
    client.publish("testing_raspbians", command)


def power_off_pi():
    aiy.audio.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)


def reboot_pi():
    aiy.audio.say('See you in a bit!')
    subprocess.call('sudo reboot', shell=True)


def say_ip():
    ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    aiy.audio.say('My IP address is %s' % ip_address.decode('utf-8'))


def process_event(assistant, event):
    status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')
            time.sleep(1)
            

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status('listening')
        

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        
        if text == 'power off':
            assistant.stop_conversation()
            power_off_pi()
        elif text == 'reboot':
            assistant.stop_conversation()
            reboot_pi()
        elif text == 'ip address':
            assistant.stop_conversation()
            say_ip()
        elif text == 'move forward':
            assistant.stop_conversation()
            client.publish("testing_raspbians", "i")  # keyboard control "i" for car forward
         
           
        elif text == 'turn right':
            assistant.stop_conversation()
            client.publish("testing_raspbians", "l")  # keyboard control "l" for car forward
            
        elif text == 'turn left':
            assistant.stop_conversation()
            client.publish("testing_raspbians", "j")  # keyboard control "j" for car forward
            
        elif text == 'move back':
            assistant.stop_conversation()
            client.publish("testing_raspbians", "m")  # keyboard control "l" for car forward 
        elif text == 'stop':
            assistant.stop_conversation()
            client.publish("testing_raspbians", "k")  # keyboard control "k" for car forward
            
        elif text == 'red lights':
            assistant.stop_conversation()
            client.publish("testing_raspbians", "red")  # rgb-led control
        elif text == 'green lights':
            assistant.stop_conversation()
            client.publish("testing_raspbians", "green")  # rgb-led control
        
        elif text == 'blue lights':
            assistant.stop_conversation()
            client.publish("testing_raspbians", "blue")  # rgb-led control
        
        elif text == 'animation':
            assistant.stop_conversation()
            client.publish("testing_raspbians", "rainbow")  # rgb-led control
        
        elif text == 'no lights':
            assistant.stop_conversation()
            client.publish("testing_raspbians", "nolight")  # rgb-led control


    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')
        
    elif event.type == EventType.ON_CONVERSATION_TURN_FINISHED:
        status_ui.status('ready')
        

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            byte = str(randint(0,4)).encode("utf-8")
            ser.write(byte)
            process_event(assistant, event)


if __name__ == '__main__':
    main()

