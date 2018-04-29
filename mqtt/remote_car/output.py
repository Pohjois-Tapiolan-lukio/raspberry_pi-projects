import paho.mqtt.client as mqtt
from time import sleep

def send_message(client):
    print("Auton kommennot: j = vasemmalle, i=eteenpain, k=stop,  l=oikealle ja m=taakse\n")
    print("Lednauhan ohjaus: red, green, blue, white, nolight, rainbow")
    command = input("anna auton tai lednauhan ohjauskomento: j, i, k, l, m\n")
    
    client.publish("testing_raspbians", command)

def main():
    try:
        client = mqtt.Client(client_id = "<your device name>")
        client.username_pw_set("<User>", password = "<Password>")
        client.connect("broker.shiftr.io", 1883, 60)
        client.loop_start()
        while True:
            send_message(client)
            sleep(1)
    except keyboardInterrupt:
        print("Ohjelman suoritus paattyy.")
if __name__ == "__main__":
    main()
