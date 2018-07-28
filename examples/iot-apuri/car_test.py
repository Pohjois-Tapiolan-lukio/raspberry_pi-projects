import iot
from time import sleep
# from l293d_pwm import L293DPWM
from drv8835 import DRV8835
# from testing_motor import TestingMotorDriver

# car = L293DPWM(17, 27, 26, 23, 24, 6)
# car = L293DPWM(24, 12, 26, 13, 5, 6)
car = DRV8835()

car.stop()

@iot.subscribe("automessages")
def new_message(message):
    if (message == "moveforward"):
        car.forward(100,100)
        sleep(2)
        car.stop()
    elif (message == "movebackward"):
        car.backward(100,100)
        sleep(2)
        car.stop()
    elif (message == "moveright"):
        car.backward(100,25)
        sleep(2)
        car.stop()
    elif (message == "moveleft"):
        car.backward(25,100)
        sleep(2)
        car.stop()
        
iot.run("Raspberryauto", "shiftr-key", "shiftr-secret")

'''
car.stop()
car.forward(100, 100)
print("forward")
sleep(2)
car.stop()
car.backward(100,100)
print("back")
sleep(2)
car.forward(25,100)
print("Left")
sleep(1)
car.stop()
car.forward(100,25)
print("Right")
sleep(2)
car.stop()
'''