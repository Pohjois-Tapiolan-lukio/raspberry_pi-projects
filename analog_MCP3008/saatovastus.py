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

output valilla 0...1
'''
from gpiozero import MCP3008
import time

saatovastus = MCP3008(channel =0)

print("ctrl +C lopettaa ohjelman")

try:
	while True:
		lukema = saatovastus.value
		print("{:.2f}".format(lukema))
		#print(lukema)
		time.sleep(1)
except KeyboardInterrupt:
	print(" Lopetetaan ohjelma")
