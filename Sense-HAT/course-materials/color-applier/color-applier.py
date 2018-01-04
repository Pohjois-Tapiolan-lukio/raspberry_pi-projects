from sense_hat import SenseHat

sense = SenseHat()

def apply_color(r, g, b):
    pixel_list = []
    for i in range(8 * 8):
        pixel_list.append([r, g, b])
    sense.set_pixels(pixel_list)

print("Värin punaisuus (0-255):")
r = int(input())
print("Värin vihreys (0-255):")
g = int(input())
print("Värin sinisyys (0-255):")
b = int(input())
apply_color(r, g, b)
