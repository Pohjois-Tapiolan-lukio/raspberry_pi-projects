# -*- coding: utf-8 -*-
from picamera import PiCamera
from time import sleep
from flask import Flask, Response
import classify_image

app = Flask(__name__) # Luo Flask-olio

camera = PiCamera() # Luo kamera-olio
camera.resolution = (1280, 720) # Aseta kameran resoluutio
camera.framerate = 24 # Aseta kameran päivitystaajuus


def take_picture(): # Ottaa kuvan ja palauttaa sen
    camera.capture(".temp.jpeg", use_video_port = True) # Ota kuva kameralla (videomodessa, ottaa kuvia luultavasti hieman nopeammin)
    with open(".temp.jpeg", "rb") as file: # Avaa tiedosto ".temp.jpeg" (minne edellinen rivi tallensi kuvansa)
        data = file.read() # Lue tiedoston sisältö muuttujaan data
    return data # Palauta luettu data


def new_frame(): # Luo uuden framen "videota"
    while True: # Luo ikuinen generaattori
        data = take_picture() # Ota kuva

        # Palauta yksi frame (yieldiä varten etsi python generators) joka sisältää boundary-merkinnän "--frame" ja datan
        # HTTP-protokollan vaatimassa muodossa (Content-Type määritelty ja rivinvaihtoja sopiva määrä)
        yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + data + b"\r\n")


# Kerro Flaskille (eli app-oliolle) että tässä on funktio joka palauttaa sen mitä löytyy osoitteesta "http://0.0.0.0/video"
# (Vain loppuosa /video tarvitsee määritellä, sillä alkuosa määritellään tiedoston lopussa)
@app.route("/video")
def video():
    # Palauta Response-olio (Flaskin luoma luokka joka sisältää tietoa liittyen HTTP-vastaukseen)
    # (Ensimmäinen parametri on itse data, toinen on sen datan ns. tyyppi. multipart/x-mixed-replace on tyyppi,
    #  boundary=frame määrittelee sille tyypille sen, että "--frame" erottelee eri framet)
    return Response(new_frame(), mimetype = "multipart/x-mixed-replace; boundary=frame")

# Kts. video()
@app.route("/picture")
def picture():
    return Response(take_picture(), mimetype = "image/jpeg")

# Luo pieni html pohja
def create_html(content):
    return "<html><head><meta charset='utf-8'><title>Classifier</title></head><body>" + content + "</body></html>"

# Kts. video()
@app.route("/")
def index():
    # Tämä on yksinkertainen sivu jolle ei tarvitse määritellä tyyppiä, joten voimme palauttaa suoraan datana.
    return create_html("<a href='/classify'><button>Classify!</button></a>")

# Kts. video()
@app.route("/classify")
def classify():
    print("Starting classification...")
    take_picture()
    description = classify_image.classify(".temp.jpeg")
    print("Picture classified!")
    return create_html("<h2>" + description + "</h2><img src='/picture'></img>")

# Valmista classify
classify_image.maybe_download_and_extract()

# Käynnistä Flask-palvelin ip:hen 0.0.0.0 (eli kaikki requestit jota Pi:lle tulee otetaan vastaan)
# ja porttiin 80 (standardi HTTP-portti, vaatii sudolla pyörittämisen)
app.run(host = "0.0.0.0", port = 80)
