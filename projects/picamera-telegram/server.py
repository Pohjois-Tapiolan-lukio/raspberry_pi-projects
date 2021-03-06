from flask import Flask
import requests
import picamera

app = Flask(__name__)
TOKEN = ''

@app.route('/photo', methods=['GET','POST'])
def handle_photo():
    camera_capture()
    send_to_telegram(TOKEN)
    return '{"success":"true"}'

def camera_capture():
    with picamera.PiCamera() as camera:
        with open('image.jpg', 'wb') as capture_file:
            camera.capture(capture_file)

def send_to_telegram(token=''):
    if token == '':
    	raise Exception('Telegram bot token not specified!')
    with open('image.jpg', 'rb') as capture_file:
        url = 'https://api.telegram.org/bot{}/sendPhoto'.format(token)
        f = {"photo": capture_file}
        p = {'chat_id': <your chat id>}
        res = requests.post(url, files=f, params=p)

app.run(host="0.0.0.0")
