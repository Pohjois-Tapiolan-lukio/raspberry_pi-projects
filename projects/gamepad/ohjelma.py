#!/usr/bin/env python3

# Tuodaan ohjelmaan sarjaliikennemoduuli,
# saannollisten lausekkeiden moduuli ja
# uinput moduuli
import serial, re, uinput

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

# Luodaan uinput.Device-olio nimelta gamepad
with uinput.Device([
    uinput.ABS_X,
    uinput.ABS_Y,
    uinput.BTN_SOUTH]) as gamepad:
    # Yritetaan ajaa koodi kunnes napataa KeyboardInterrupt-olio
    try:
        while True:
            # Luetaan sarjaliikennetta
            rivi = ser.readline().decode('ascii').strip('\r\n')
            # Ryhmitellaan rivin data
            groups = dataRe.findall(rivi)
            if not groups:
                print("Rikkinaista dataa {}".format(rivi))
                # Jatka seuraavaan while-silmukan iteraatioon
                # (skippaa alla olevan koodin)
                continue
            # Muutetaan groups-listan ensimmaisen alkion alkiot inteiksi
            groups = [int(arvo) for arvo in groups[0]]

            # Muutetaan oikeaan skaalaan
            ABS_X = 32767 - 65535 * groups[0]//1023
            ABS_Y = 32767 - 65535 * groups[1]//1023
            BTN_SOUTH = 1 - groups[2]

            print(ABS_X, ABS_Y, BTN_SOUTH)

            # Emittoidaan tapahtumat
            gamepad.emit(uinput.ABS_X, ABS_X)
            gamepad.emit(uinput.ABS_Y, ABS_Y)
            gamepad.emit(uinput.BTN_SOUTH, BTN_SOUTH)
    except KeyboardInterrupt:
        # Suljetaan sarjaliikennevayla
        ser.close()
        print(" Ohjelma suljetaan")

# vim: et ts=4 sw=4 :
