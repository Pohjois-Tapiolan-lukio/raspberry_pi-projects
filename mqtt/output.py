import paho.mqtt.client as mqtt
from time import sleep

def send_message(client):
    client.publish("testing_raspbians", "Ping!")

def main():
    client = mqtt.Client(client_id = "raspberry_out")
    client.username_pw_set("52232dae", password = "0e9f7409a5dace08")
    client.connect("broker.shiftr.io", 1883, 60)
    client.loop_start()
    while True:
        send_message(client)
        sleep(1)

if __name__ == "__main__":
    main()
