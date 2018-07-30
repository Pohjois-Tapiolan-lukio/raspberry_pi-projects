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
# testaa komennolla ls -l /deb/tty* microbitin usb-kytkennalla ja ilman!
laite = "/dev/ttyACM0"


# Luodaan Serial-olio
ser = serial.Serial(laite, baudrate=115200, timeout=1)

# Luodaan valmis Re-olio
# dataRe = re.compile(r"^(\d{1,4}),(\d{1,4}),([01])$")
dataRe = re.compile(r"^\s*(-?\d+[?:[.]\d+]?)\s+(-?\d+[?:[.]\d+]?)$")

# car = L293DPWM(17, 27, 26, 23, 24, 6)
# car = L293DPWM(24, 12, 26, 13, 5, 6)
car = DRV8835()  # if Polulu motor driver for raspberry is used

def maxmin(arvo, maks, minn):
    return max(min(arvo, maks), minn)

arvot = []
active = True
def serial_read():
    print("Serial_thread kaynnistetty")
    global arvot
    while active:
        # Luetaan sarjaliikennetta
        rivi = ser.readline().decode('ascii').strip('\r\n')
        # Ryhmitellaan rivin data
        groups = dataRe.findall(rivi)
        if not groups:
            #print("Rikkinaista dataa {}".format(rivi))
            # Jatka seuraavaan while-silmukan iteraatioon
            # (skippaa alla olevan koodin)
            continue
        arvot = [float(x) for x in groups[0]]
        # [1.32323, 5.23423]
        #Warning: if you use print, yuor threads won't sync
        #print(arvot)
        
       
       
def drive_car():
    print("Car_thread kaynnistetty")
    from numpy import sign
    while active:
        if arvot:
            kaannos = 30*arvot[1]/45.0 # or /90.0
            kaasu = 100*arvot[0]/45.0
            suunta = sign(kaasu)
            motorLeft = maxmin(int(kaasu-suunta*kaannos),100,-100)
            motorRight = maxmin(int(kaasu+suunta*kaannos),100,-100)

            car.forward(motorLeft, motorRight)

       
try:
    # usb-serialin lukeminen ja auton ohjaaminen ovat rinnakkaisia prosesseja.
    # serialista tulee uutta dataa nopeasti, auton ohjaaminen on forward hitaampi prosessi.
    # Auto lukee serialista aina viimeisimmat ohjausarvot.
    serial_thread = Thread(target = serial_read)
    
    car_thread = Thread(target = drive_car)
    serial_thread.start()
    car_thread.start()
    while 1:
        # odota etta tulee CTRL-C
        pass

except:
    # Suljetaan sarjaliikennevayla
    active = False
    serial_thread.join()
    car_thread.join()
    ser.close()
    car.stop()
    print(" Ohjelma suljetaan")
