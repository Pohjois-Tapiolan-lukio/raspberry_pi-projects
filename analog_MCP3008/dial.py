from gpiozero import MCP3008 
import time

class dial:
    def __init__(self):
        self.conn = MCP3008(channel =0) 

   # def bitstring(self, n): 
       # s = bin(n)[2:] 
       #return '0'*(8-len(s)) + s 

    def get(self):
	    return  float(self.conn.value)

if __name__ == '__main__': 
	dial=dial()
	try:   
		while True:	
			print(dial.get())
	except KeyboardInterrupt:
		print("suoritus paattyy")
