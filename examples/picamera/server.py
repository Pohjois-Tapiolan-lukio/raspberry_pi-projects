from flask import Flask, Response
import picamera

app = Flask(__name__)

@app.route('/')
def handle_photo():
    file = camera_capture()
    return Response(file, mimetype="image/jpg")


def camera_capture():
    with picamera.PiCamera() as camera:
        camera.capture("image.jpg")
        with open('image.jpg', 'rb') as capture_file:
            picture = capture_file.read()
    return picture


app.run(host="0.0.0.0",port=5000)
