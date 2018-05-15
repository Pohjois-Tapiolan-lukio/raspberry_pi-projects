import paho.mqtt.client as mqtt
from time import sleep

def send_message(client):
    client.publish("testing_raspbians", "Ping!")

def main():
    client = mqtt.Client(client_id = "<your cliet_id>")
    client.username_pw_set("<your username, Key>", password = "<your passwd>")
    client.connect("broker.shiftr.io", 1883, 60)
    client.loop_start()
    while True:
        send_message(client)
        sleep(1)

if __name__ == "__main__":
    main()
