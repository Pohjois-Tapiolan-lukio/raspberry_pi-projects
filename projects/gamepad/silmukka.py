#!/usr/bin/env python3

# Tuodaan ohjelmaan sarjaliikennemoduuli
import serial

# Maariteellaan Arduinon merkkilaitteen sijainti
laite = "/dev/ttyACM0"

# Ala resetoi Arduinoa seriaaliyhteyden sulkeutuessa
# Disable reset after hangup
with open(laite) as f:
    import termios
    attrs = termios.tcgetattr(f)
    attrs[2] = attrs[2] & ~termios.HUPCL
    termios.tcsetattr(f, termios.TCSAFLUSH, attrs)

# Luodaan Serial-olio
ser = serial.Serial(laite, baudrate=9600, timeout=1)

# Yritetaan ajaa koodi kunnes napataa KeyboardInterrupt-olio
try:
    while True:
        # Luetaan sarjaliikennetta
        rivi = ser.readline()
        print(rivi)
except KeyboardInterrupt:
    # Suljetaan sarjaliikennevayla
    ser.close()
    print(" Ohjelma suljetaan")

# vim: et ts=4 sw=4 :
