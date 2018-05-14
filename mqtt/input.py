import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Yhdistettiin koodilla:", str(rc))
    client.subscribe("testing_raspbians")

def on_message(client, userdata, msg):
    print(msg.topic, str(msg.payload))

def main():
    client = mqtt.Client(client_id = "raspberry_in")
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("52232dae", password = "0e9f7409a5dace08")
    client.connect("broker.shiftr.io", 1883, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()
