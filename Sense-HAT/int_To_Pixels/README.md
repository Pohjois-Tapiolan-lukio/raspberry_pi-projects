# Module to convert intigers (00-99) to pixel arrays which can be draw to Sense HAT modules 8x8 pixel screen. 
**Put** `int_To_Pixels.py` in to your **project folder**.  
**Use** `from int_To_Pixels import intToPixels` To **import** the module to your code.  
  
   
This **[example](https://github.com/Pohjois-Tapiolan-lukio/raspberry_pi-projects/blob/master/Sense-HAT/int_To_Pixels/example.py)** can be found at the **[github folder](https://github.com/Pohjois-Tapiolan-lukio/raspberry_pi-projects/tree/master/Sense-HAT/int_To_Pixels)**.  
  
```Python
# Exaple to print number 50 to Sense HAT modules screen on red color 

from sense_hat import SenseHat
from int_To_Pixels import intToPixels

sense = SenseHat()

# intToPixels(Intiger, foreground color as [R, G, B], background color as [R, G, B])
sense.set_pixels(intToPixels(50, [255, 0, 0], [0, 0, 0]))
```
