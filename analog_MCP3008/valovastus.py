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
