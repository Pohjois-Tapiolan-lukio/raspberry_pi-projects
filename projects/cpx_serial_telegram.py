'''
Palvelinskripti, joka lahettaa sykkeen telegrammiin
ennalta maaritetylle telegram-botille
'''

#from flask import Flask
import requests
#import picamera
import os
import serial
import io
#import time

ser = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=115200)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

#ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)

heartbeats_to_telegram = []
heartbeats_to_telegram.append(0)

BOT_API_TOKEN = 'INSERT YOUR TOKEN'
GROUP_ID = 'INSERT YOUR GROUP_ID'
TG_URL = 'https://api.telegram.org/bot'+ BOT_API_TOKEN


#app = Flask(__name__)

while True:
        serial_in = int(sio.readline())
        print('Found in serial: ' + str(serial_in))
        if serial_in > 45 and serial_in < 120:
            #print('this is beat will be sent to telegram')
            if serial_in not in heartbeats_to_telegram:
                url = TG_URL + '/sendMessage'
                telegram_message = 'Your current heartbeat (bpm): ' + str(serial_in)
                res = requests.post(url, params={'chat_id': GROUP_ID}, data ={'text': telegram_message})
                heartbeats_to_telegram.append(serial_in)
            #handle_message(serial_in)
        #time.sleep(0.5)
'''
@app.route('/message', methods=['GET','POST'])
def handle_message(message):
    url = TG_URL + '/sendMessage'
    res = requests.post(url, params={'chat_id': GROUP_ID}, data ={'text': message})
    return '{"success":"true"}'



@app.route('/photo', methods=['GET','POST'])
def handle_photo():
    camera_capture('image.jpg', 'photo')
    send_to_telegram('image.jpg', 'photo')
    return '{"success":"true"}'

@app.route('/video', methods=['GET','POST'])
def handle_video():
    camera_capture('video.h264', 'video', length=4)
    convert_h264_to_mp4()
    send_to_telegram('video.mp4', 'video')
    return '{"success":"true"}'

def convert_h264_to_mp4():
    """ Muuntaa raa'an .h264 videon mp4:ksi MP4Box:n avulla.
        Huom! Vaatii koneelta GPAC-binaarit.
        >> sudo apt-get update
        >> sudo apt-get install gpac """
    os.system('rm video.mp4')
    os.system('MP4Box -add video.h264:fps=24 video.mp4')
    os.system('rm video.h264')

def camera_capture(filename, type, length=3):
    with picamera.PiCamera() as camera:
        with open(filename, 'wb') as capture_file:
            """ Lisaa kamera-asetuksia voi muokata tahan.
                https://picamera.readthedocs.io/en/release-1.12/api_camera.html """
            camera.hflip = True # kaanna vaaka-akselin suhteen
            camera.vflip = True # peilikuva
            if type == 'photo':
                camera.resolution = (1296, 972)
                camera.capture(capture_file)
            elif type == 'video':
                camera.resolution = (640, 480)
                camera.framerate = 24
                camera.start_recording(capture_file)
                camera.wait_recording(length)
                camera.stop_recording()

def send_to_telegram(filename, type):
    """ Funktio lahettaa telegramiin tyypista riippuen 
        kuvan tai videon. """
    with open(filename, 'rb') as capture_file:
        if type == 'photo':
            url = TG_URL + '/sendPhoto'
            files = {"photo": capture_file}
        elif type == 'video':
            url = TG_URL + '/sendVideo'
            files = {"video": capture_file}
        res = requests.post(url, files=files, params={'chat_id': GROUP_ID})
'''
if __name__ ==  '__main__':
    app.run(host="0.0.0.0")

