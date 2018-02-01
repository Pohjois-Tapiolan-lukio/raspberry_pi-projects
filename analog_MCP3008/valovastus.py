from MCP3008 import MCP3008
valovastus = MCP3008()
lukema = valovastus.read(channel =0))

print("  {:.2f}".format(lukema)) 
