#!/usr/bin/env python3

# Tuodaan ohjelmaan sarjaliikennemoduuli ja
# saannollisten lausekkeiden moduuli
import serial, re

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

# Luodaan valmis Re-olio
dataRe = re.compile(r"^(\d{1,4}),(\d{1,4}),([01])$")

# Yritetaan ajaa koodi kunnes napataa KeyboardInterrupt-olio
try:
    while True:
        # Luetaan sarjaliikennetta
        rivi = ser.readline().decode('ascii').strip('\r\n')
        # Ryhmitellaan rivin data
        groups = dataRe.findall(rivi)
        if not groups: # jos groups on []
            print("Rikkinaista dataa {}".format(rivi))
            # Jatka seuraavaan while-silmukan iteraatioon
            # (skippaa alla olevan koodin)
            continue
        print(groups)
except KeyboardInterrupt:
    # Suljetaan sarjaliikennevayla
    ser.close()
    print(" Ohjelma suljetaan")

# vim: et ts=4 sw=4 :
