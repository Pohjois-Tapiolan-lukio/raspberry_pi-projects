import spidev 

class dial:
    def __init__(self, device=0, channel=0):
        self.conn = spidev.SpiDev(device, channel) 
 
    def bitstring(self, n): 
        s = bin(n)[2:] 
        return '0'*(8-len(s)) + s 
    
    def get(self):
        reply_bytes = self.conn.xfer2([128, 0])
        reply_bitstring = ''.join(self.bitstring(n) for n in reply_bytes) 
        return int(reply_bitstring, 2)/2048.0

if __name__ == '__main__': 
   dial=dial()
   print dial.get()
