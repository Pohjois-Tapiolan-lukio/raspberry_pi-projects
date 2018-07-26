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

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import platform
import subprocess
import sys
import requests


from googletrans import Translator

import aiy.assistant.auth_helpers
from aiy.assistant.library import Assistant
import aiy.audio
import aiy.voicehat
from google.assistant.library.event import EventType
aiy.i18n.set_language_code('de-DE')

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

translator = Translator()
phrases = {}

def power_off_pi():
    aiy.audio.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)

def rehearsal():
    for key in phrases:
        aiy.audio.say(key+ ' is ', lang= 'en-US')
        aiy.audio.say(phrases[key], lang = 'de-DE')
    

def reboot_pi():
    aiy.audio.say('See you in a bit!')
    subprocess.call('sudo reboot', shell=True)

def make_translation(translation_text, src, dest):
    translated_text = translator.translate(translation_text, src = src, dest = dest).text
    if src == 'en':
        phrases[translation_text] = translated_text
    else:
        phrases[translated_text] = translation_text
    print(phrases)
    payload = {}
    payload['value1'] = translation_text
    payload['value2'] = translated_text
    response = requests.post("https://maker.ifttt.com/trigger/dictPost/with/key/g0O0YXMjT_Kr3X4Wf5fzSGrPVHesJjHSZK1J13kQQRW", data = payload)
    return translated_text


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
        print(text)
        if 'in german' in text:
            #lang = 'de'
            if 'what is the meaning for' in text:
                translation_text = text[23: -9]
                print(translation_text)
                print(make_translation(translation_text, src='de', dest='en'))
            elif 'translate' in text:
                translation_text = text[9: -9]
                print(translation_text)
                print(make_translation(translation_text, src ='en', dest='de'))
        if 'in swedish' in text:
            lang = 'sv'
            if 'what is the meaning for' in text:
                translation_text = text[23: -10] 
                print(make_translation(translation_text, src='sv', dest ='de'))
            elif 'translate' in text:
                translation_text = text[9: -10]
                print(translation_text)
                print(make_translation(translation_text, src ='en', dest='sv'))
        elif text == 'rehearsal':
            assistant.stop_conversation()
            rehearsal()
        


    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')

    elif (event.type == EventType.ON_CONVERSATION_TURN_FINISHED
          or event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT
          or event.type == EventType.ON_NO_RESPONSE):
        status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)

  
   
def main():
    if platform.machine() == 'armv6l':
        print('Cannot run hotword demo on Pi Zero!')
        exit(-1)

    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)


if __name__ == '__main__':
    main()
