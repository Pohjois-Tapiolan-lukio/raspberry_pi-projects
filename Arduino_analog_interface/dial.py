import serial
import time

class dial:
    def __init__(self, device='/dev/ttyACM0', boundrate=9600):
        self.conn = serial.Serial(device, boundrate) 

   # def bitstring(self, n): 
       # s = bin(n)[2:] 
       #return '0'*(8-len(s)) + s 

    def get(self):
	#reply_bytes = self.conn.xfer2([128, 0])
        #reply_bitstring = ''.join(self.bitstring(n) for n in reply_bytes) 
        time.sleep(0.01)
	return  float(self.conn.readline())/1023

if __name__ == '__main__': 
	dial=dial()
	try:   
		while True:	
			print(dial.get())
	except KeyboardInterrupt:
		print("suoritus paattyy")
