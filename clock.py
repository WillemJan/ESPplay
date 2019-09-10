import time
import apa102

from machine import Pin
from neopixel import NeoPixel
from machine import RTC


'''
strip = apa102.APA102(Pin(5), Pin(4), 37)

brightness = 1  # 0 is off, 1 is dim, 31 is max

# Helper for converting 0-255 offset to a colour tuple
def wheel(offset, brightness):
    # The colours are a transition r - g - b - back to r
    offset = 255 - offset
    if offset < 85:
        return (255 - offset * 3, 0, offset * 3, brightness)
    if offset < 170:
        offset -= 85
        return (0, offset * 3, 255 - offset * 3, brightness)
    offset -= 170
    return (offset * 3, 255 - offset * 3, 0, brightness)

# Demo 1: RGB RGB RGB
'''

rtc = RTC()
rtc.datetime((2019, 9, 1, 10, 49, 0, 0, 0)) # set a specific date and time


t = 0

pin = Pin(0, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 32)   # create NeoPixel driver on GPIO0 for 8 pixels

while True:
    ct = rtc.datetime()
    ch = ct[3]
    for i in range(32):
        np[i] = (0,0,0)

    for i in range(32):
        if i == ch or i == ch +1:
            np[i] = (0,0,255)
        elif i == t:
            np[i] = (0,255,0)

    np.write()
    time.sleep(0.004)

    if t == 32:
        t = 0
    else:
        t += 1

    '''
    red = 0xff0000
    green = red >> 8
    blue = red >> 16
    for i in range(strip.n):
	colour = red >> (i % 3) * 8
	strip[i] = ((colour & red) >> 16, (colour & green) >> 8, (colour & blue), brightness)
    strip.write()

    # Demo 2: Show all colours of the rainbow
    for i in range(strip.n):
	strip[i] = wheel((i * 256 // strip.n) % 255, brightness)
    strip.write()

    # Demo 3: Fade all pixels together through rainbow colours, offset each pixel
    for r in range(5):
	for n in range(256):
	    for i in range(strip.n):
		strip[i] = wheel(((i * 256 // strip.n) + n) & 255, brightness)
	    strip.write()
	time.sleep_ms(25)

    # Demo 4: Same colour, different brightness levels
    for b in range(31,-1,-1):
	strip[0] = (255, 153, 0, b)
	strip.write()
	time.sleep_ms(250)

    # End: Turn off all the LEDs
    strip.fill((0, 0, 0, 0))
    strip.write()
    '''
