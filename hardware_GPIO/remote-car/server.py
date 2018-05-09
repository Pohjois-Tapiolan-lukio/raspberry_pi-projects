#import RPi.GPIO as GPIO
import time
import picamera
from flask import Flask, Response
from l293d_pwm import L293DPWM
import atexit

# See README.md for pinout
# 2A = GPIO17, 1A = GPIO27, 1,2EN = LEFT_PWM  = GPIO26
# 4A = GPIO23, 3A = GPIO24, 3,4EN = RIGHT_PWM = GPIO06
car = L293DPWM(17, 27, 26, 23, 24, 6)
car.stop()

app = Flask(__name__)

camera = picamera.PiCamera()
camera.resolution = (320, 180)
camera.framerate = 80
camera.hflip = True
def close_camera():
    camera.close()

atexit.register(close_camera)

with open("index.html", "r") as file:
    html = file.read()
with open("index.js", "r") as file:
    js = file.read()

@app.route("/")
def index():
    return html
@app.route("/index.js")
def index_js():
    return js

def take_picture():
    camera.capture(".temp.jpeg", use_video_port = True)
    with open(".temp.jpeg", "rb") as file:
        data = file.read()
    return data

def new_frame():
    while True:
        data = take_picture()
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + data + b"\r\n")


@app.route("/video_feed")
def video_feed():
    return Response(new_frame(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/video_feed_single")
def video_feed_single():
    return Response(take_picture(),
                    mimetype="image/jpeg")

@app.route("/forward")
def forward():
    car.forward(100, 100)
    return "Moving forward"

@app.route("/backward")
def backward():
    car.backward(100, 100)
    return "Moving backward"

@app.route("/left")
def left():
    car.forward(25, 100)
    return "Moving left"

@app.route("/right")
def right():
    car.forward(100, 25)
    return "Moving right"

@app.route("/stop")
def stop():
    car.stop()
    return "Stopping"


app.run(host = "0.0.0.0", port = 80)
