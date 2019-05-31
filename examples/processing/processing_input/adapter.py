import time
import serial
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(msg.topic,str(msg.payload))

CHANNEL="ledUpdate"



ser = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=115200)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

# Käytä omaa shiftriä
# Tässä käytössä oleva on https://shiftr.io/kameli/processing

client = mqtt.Client(client_id="raspberry_adapter")
client.username_pw_set("testi-processing", password="testi-processing")
client.connect("broker.shiftr.io", 1883, 60)
client.on_message=on_message

client.subscribe(CHANNEL)

client.loop_forever()

