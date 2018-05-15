from time import sleep
from l293d_pwm import L293DPWM

#car = L293DPWM(17, 27, 26, 23, 24, 6)
car = L293DPWM(24, 12, 26, 13, 5, 6)

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
