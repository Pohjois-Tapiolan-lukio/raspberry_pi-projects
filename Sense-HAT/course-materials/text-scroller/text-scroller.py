from sense_hat import SenseHat

sense = SenseHat()

print("Kirjoita esitettävä teksti:")
text = input()
sense.show_message(text)
