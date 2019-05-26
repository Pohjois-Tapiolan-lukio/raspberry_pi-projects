import iot
import picamera
import requests




BOT_API_TOKEN =<Insert Your Api token>
GROUP_ID = <insert your group id>
TG_URL = 'https://api.telegram.org/bot'+ BOT_API_TOKEN



@iot.listen("selfie")
def selfie():
    take_pic()

def take_pic():
    iot.say("Taking a selfie!")
    with picamera.PiCamera():
        with open("image.jpg", 'wb') as capture_file:
            camera.hflip = True # kaanna vaaka-akselin suhteen
            camera.vflip = True # peilikuva
            camera.resolution = (1296, 972)
            camera.capture(capture_file)
    
    with open(filename, 'rb') as capture_file:
        url = TG_URL + '/sendPhoto'
        files = {"photo": capture_file}
        res = requests.post(url, files=files, params={'chat_id': GROUP_ID})
iot.run()


