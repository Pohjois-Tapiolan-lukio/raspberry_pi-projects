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
