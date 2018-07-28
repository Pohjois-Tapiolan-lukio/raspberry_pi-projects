# Usb-kaapelilla autoon kytketyn kiihtyvyysanturi toimii auton
# ohjaimena. Kallistele microbittia.
# Tyo havainnollistaa Raspberry pi:n ja microbitin valista vuorovaikutusta
# usb-serialin kautta
from time import sleep
# from l293d_pwm import L293DPWM
from drv8835 import DRV8835
# from testing_motor import TestingMotorDriver

#!/usr/bin/env python3

# Tuodaan ohjelmaan sarjaliikennemoduuli,
# saannollisten lausekkeiden moduuli ja
# uinput moduuli
import serial, re

from threading import Thread

# Maariteellaan Arduinon merkkilaitteen sijainti
laite = "/dev/ttyACM0"

# Ala resetoi Arduinoa seriaaliyhteyden sulkeutuessa
# Disable reset after hangup

#with open(laite) as f:
#    import termios
#    attrs = termios.tcgetattr(f)
#    attrs[2] = attrs[2] & ~termios.HUPCL
#    termios.tcsetattr(f, termios.TCSAFLUSH, attrs)

# Luodaan Serial-olio
ser = serial.Serial(laite, baudrate=115200, timeout=1)

# Luodaan valmis Re-olio
# dataRe = re.compile(r"^(\d{1,4}),(\d{1,4}),([01])$")
dataRe = re.compile(r"^\s*(-?\d+[?:[.]\d+]?)\s+(-?\d+[?:[.]\d+]?)$")

# car = L293DPWM(17, 27, 26, 23, 24, 6)
# car = L293DPWM(24, 12, 26, 13, 5, 6)
car = DRV8835()

def maxmin(arvo, maks, minn):
    return max(min(arvo, maks), minn)

arvot = []
active = True
def serial_read():
    global arvot
    while active:
        # Luetaan sarjaliikennetta
        rivi = ser.readline().decode('ascii').strip('\r\n')
        # Ryhmitellaan rivin data
        groups = dataRe.findall(rivi)
        if not groups:
            print("Rikkinaista dataa {}".format(rivi))
            # Jatka seuraavaan while-silmukan iteraatioon
            # (skippaa alla olevan koodin)
            continue
        arvot = [float(x) for x in groups[0]]
        # [1.32323, 5.23423]
        # print(arvot)
        
       
       
def drive_car():       
    while active:
        if arvot:
            kaannos = int(30*arvot[1]/90.0)
            car.forward(maxmin(int(100*arvot[0]/90.0)-kaannos,100,-100),
                    maxmin(int(100*arvot[0]/90.0)+kaannos,100,-100))
       
       
       
try:
    # usb-serialin lukeminen ja auton ohjaaminen ovat rinnakkaisia prosesseja.
    # serialista tulee uutta dataa nopeasti, auton ohjaaminen on forward hitaampi prosessi.
    # Auto lukee serialista aina viimeisimmat ohjausarvot.
    serial_thread = Thread(target = serial_read)
    
    car_thread = Thread(target = drive_car)
    serial_thread.start()
    car_thread.start()
 
except KeyboardInterrupt:
    # Suljetaan sarjaliikennevayla
    active = False
    ser.close()
    car.stop()
    print(" Ohjelma suljetaan")
    
'''
# testikoodi auton kytkentojen testaukseen.
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