#!/usr/bin/env python3
import serial

laite = "/dev/ttyACM0"

# Ala resetoi Arduinoa seriaaliyhteyden sulkeutuessa
# Disable reset after hangup
with open(laite) as f:
    import termios
    attrs = termios.tcgetattr(f)
    attrs[2] = attrs[2] & ~termios.HUPCL
    termios.tcsetattr(f, termios.TCSAFLUSH, attrs)

ser = serial.Serial(laite, baudrate=9600, timeout=1)

try:
    while True:
        rivi = ser.readline()
        print(rivi)
except KeyboardInterrupt:
    ser.close()
    print(" Ohjelma suljetaan")

# vim: et ts=4 sw=4 :
