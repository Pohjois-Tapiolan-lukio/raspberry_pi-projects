#import RPi.GPIO as GPIO
import time
from flask import Flask, Response
from l293d_pwm import L293DPWM

car = L293DPWM(24, 12, 26, 13, 5, 6)
car.stop()

app = Flask(__name__)


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

# TODO: PiCamera
def gen_frame():
    while True:
        frame = b""
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

@app.route("/video_feed")
def video_feed():
    return Response(gen_frame(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/forward")
def forward():
    car.forward(90, 100)
    return "Moving forward"

@app.route("/backward")
def backward():
    car.backward(90, 100)
    return "Moving backward"

@app.route("/left")
def left():
    car.forward(50, 100)
    return "Moving left"

@app.route("/right")
def right():
    car.forward(100, 50)
    return "Moving right"

@app.route("/stop")
def stop():
    car.stop()
    return "Stopping"


app.run(host = "0.0.0.0", port = 8080)
