'''
PINnit raspbyn ja dca muuntimen valissa
Raspberry--> MCP3008
Pin1 (3.3V)--> Pin16(VDD)
Pin1 --> Pin15(vref)
Pin6 (GND)--> Pin14(AGND)
Pin23(Sclk)-->Pin13(CLK)
Pin21(MISO)--> Pin12 (DOUT)
Pin19(MOSI)--> Pin11 (DIN)
Pin 24 (CE0) --> Pin10 (CS/SHDN)
Pin6(GND)-->Pin9(DGND)

ulostulo valilla 0...1023
'''
from MCP3008 import MCP3008
import time

valovastus = MCP3008()

print("ctrl +C lopettaa ohjelman")

try:
	while True:
		lukema = valovastus.read(channel =0)
		print("{:.2f}".format(lukema))
		#print(lukema)
		time.sleep(1)
except KeyboardInterrupt:
	print(" Lopetetaan ohjelma")
