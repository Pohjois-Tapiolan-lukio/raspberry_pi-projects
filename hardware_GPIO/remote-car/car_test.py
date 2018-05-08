from time import sleep
from l293d_pwm import L293DPWM

car = L293DPWM(24, 12, 26, 13, 5, 6)
car.stop()
car.forward(90, 100)
sleep(2)
car.stop()
