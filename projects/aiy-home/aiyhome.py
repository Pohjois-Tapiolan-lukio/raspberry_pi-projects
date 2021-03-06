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
# Modified by DroneBot Workshop and Matti Heikkinen
# 2018-02-20
# Modified by Jens Pitkanen
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
from time import sleep

import aiy.assistant.auth_helpers
import aiy.audio
import aiy.voicehat
from google.assistant.library import Assistant
from google.assistant.library.event import EventType

import RPi.GPIO as GPIO

PIN_LIGHTS = 13
PIN_GATE = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN_LIGHTS, GPIO.OUT)
GPIO.setup(PIN_GATE, GPIO.OUT)
# See /hardware_GPIO/servo/servo.py for the servo logic
SERVO_GATE = GPIO.PWM(PIN_GATE, 50)
SERVO_GATE.start(1)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def lights_on():
    aiy.audio.say('Rise and shine!')
    # Animate the lights on (in 0.5 seconds)
    for brightness in range(0, 11):
        GPIO.output(PIN_LIGHTS, brightness / 10.0)
        sleep(0.05)

def lights_off():
    aiy.audio.say('Good night!')
    # Animate the lights off (in 0.5 seconds)
    for brightness in range(10, -1, -1):
        GPIO.output(PIN_LIGHTS, brightness / 10.0)
        sleep(0.05)

def door_open():
    aiy.audio.say('Opening door')
    # See /hardware_GPIO/servo/servo.py for the servo logic
    SERVO_GATE.ChangeDutyCycle(7)

def door_close():
    aiy.audio.say('Closing door')
    # See /hardware_GPIO/servo/servo.py for the servo logic
    SERVO_GATE.ChangeDutyCycle(2)


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
        elif text == 'lights on':
            assistant.stop_conversation()
            lights_on()
        elif text == 'turn off':
            assistant.stop_conversation()
            lights_off()
        elif text == 'open':
            assistant.stop_conversation()
            door_open()
        elif text == 'close':
            assistant.stop_conversation()
            door_close()



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
            process_event(assistant, event)


if __name__ == '__main__':
    main()
