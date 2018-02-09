from gpiozero import MCP3008

while True:
	with MCP3008(channel =0) as pot:
		print(pot.value)
