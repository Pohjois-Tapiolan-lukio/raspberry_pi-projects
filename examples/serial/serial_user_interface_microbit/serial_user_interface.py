import time
import io
import serial

ser = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=115200)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

try:
    #ser.write(b'bong')
    while True:
        command = input("Laitetaanko valot päälle? k  = kytke, s = sammuta\n")
        if command == "k":
            ser.write(b'k')
            print("Lähetetään seriaalin tieto: k=kytke")
            serial_in = str(sio.readline())
            print(serial_in)
        elif command == "s":
            ser.write(b's')
            print("komento: s = sammutetaan")
            serial_in = str(sio.readline())
            print(serial_in)
        else:
            print("Virheellinen komento!")
        time.sleep(0.5)

except KeyboardInterrupt:
    ser.close()
    print('Ohjelman suoritus paattyy.')
