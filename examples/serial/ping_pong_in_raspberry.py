import time
import io
import serial

ser = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=115200)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

try:
    #ser.write(b'bong')
    while True:
        serial_in = str(sio.readline())
        print('Found in serial: ' + serial_in)
        if 'ping' in serial_in:
            ser.write(b'pong')
            print('wrote into serial: pong')
        time.sleep(0.5)

except KeyboardInterrupt:
    ser.close()
    print('Ohjelman suoritus paattyy.')
