import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO


from l293d_pwm import L293DPWM

# create car 
car =  L293DPWM(24, 12, 26, 13, 5, 6)
car.stop()
'''
#create addressable led-strip
from neopixel import *
# LED strip configuration:
LED_COUNT      = 10      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_RGBW
#LED_STRIP      = ws.SK6812W_STRIP

# intialiaze ledstrip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)


'''
 
def on_connect(client, userdata, flags, rc):
    print("Yhdistettiin koodilla:", str(rc))
    client.subscribe("testing_raspbians")

def on_message(client, userdata, msg):
    print(msg.topic, str(msg.payload))

    if str(msg.payload) == "i":  # move forward
        car.forward(100, 100)
        time.sleep(2)
        car.stop()
    elif  str(msg.payload) == 'l':   # turn right
        car.forward(100, 0.9*25)
        time.sleep(2)
        car.stop()
    elif str(msg.payload) == 'j':  # turn left
        car.forward(0.9*25, 100)
        time.sleep(2)
        car.stop()
    elif str(msg.payload) == 'm': # move the car backwards
        car.backward(100, 100)
        time.sleep(2)
        car.stop()
    elif str(msg.payload) == 'k':  # stop the car
        car.stop()
'''
        # led strip control
    elif str(msg.payload) == 'red': # change color red for leds
        colorWipe(strip, Color(255, 0))
    elif str(msg.payload) == 'green': # change color green for leds
        colorWipe(strip, Color(0, 0, 255))
    elif str(msg.payload) == 'blue': # change color blue for leds
        colorWipe(strip, Color(0, 255, 0))
    elif str(msg.payload) == 'white': # change color red for leds
        colorWipe(strip, Color(255, 255, 255))
    elif str(msg.payload) == 'rainbow': # change color red for leds
        colorWipe(strip, Color(255, 255, 255))
        rainbow(strip)
        rainbowCycle(strip)
    elif str(msg.payload) == 'nolights': # change color blue for leds
        colorWipe(strip, Color(0, 0, 0))
'''
def main():
    try:
        client = mqtt.Client(client_id = "raspberry_in")
        client.on_connect = on_connect
        client.on_message = on_message
        client.username_pw_set("52232dae", password = "0e9f7409a5dace08")
        client.connect("broker.shiftr.io", 1883, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        car.stop()
        colorWipe(strip, Color(0, 0, 0))
        print("Ohjelman suoritus paattyy.")
        

if __name__ == "__main__":
    main()
