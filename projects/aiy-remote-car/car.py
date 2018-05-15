import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO


from l293d_pwm import L293DPWM

SPEED = 100
LEFT = 0.7
RIGHT = 1.0

# create car
car =  L293DPWM(24, 12, 26, 13, 5, 6)
car.stop()

def on_connect(client, userdata, flags, rc):
    print("Yhdistettiin koodilla:", str(rc))
    client.subscribe("testing_raspbians")

def on_message(client, userdata, msg):
    command = str(msg.payload).lower()
    print(msg.topic, command)

    if command == "forward":  # move forward
	print("Moving forward!")
        car.forward(LEFT * SPEED * 1.0, RIGHT * SPEED * 1.0)
        time.sleep(1)
        car.stop()
    elif  command == 'right':   # turn right
	print("Turning right!")
        car.forward(LEFT * SPEED * 1.0, 0.0)
        time.sleep(1)
        car.stop()
    elif command == 'left':  # turn left
        print("Turning left!")
        car.forward(0.0, RIGHT * SPEED * 1.0)
        time.sleep(1)
        car.stop()
    elif command == 'backward': # move the car backwards
        print("Going backwards!")
        car.backward(LEFT * SPEED * 1.0, RIGHT * SPEED * 1.0)
        time.sleep(1)
        car.stop()
    elif command == 'circle':  # turn left
        print("Running in circles!")
        car.forward(LEFT * SPEED * 1.0, RIGHT * SPEED * 0.3)
        time.sleep(5)
        car.stop()
    elif command == 'stop':  # stop the car
        print("Stop!")
	car.stop()

def main():
    try:
        client = mqtt.Client(client_id = "raspberry_in")
        client.on_connect = on_connect
        client.on_message = on_message
        client.username_pw_set("52232dae", password = "0e9f7409a5dace08")
        client.connect("broker.shiftr.io", 1883, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        car.stop()
        print("Ohjelman suoritus paattyy.")


if __name__ == "__main__":
    main()
