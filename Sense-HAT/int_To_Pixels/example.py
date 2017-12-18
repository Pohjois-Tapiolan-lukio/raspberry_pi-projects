# Exaple to print number 50 to Sense HAT modules screen on red color 

from sense_hat import SenseHat
from int_To_Pixels import intToPixels

sense = SenseHat()

# intToPixels(Intiger, foreground color as [R, G, B], background color as [R, G, B])
sense.set_pixels(intToPixels(50, [255, 0, 0], [0, 0, 0]))