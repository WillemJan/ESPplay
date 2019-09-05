import machine, time
from machine import Pin
from neopixel import NeoPixel
from machine import RTC

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
        #if i == ch or i == ch +1:
        .   np[i] = (0,0,255)
        elif i == t:
            np[i] = (0,255,0)

    np.write()
    time.sleep(0.004)

    if t == 32:
        t = 0
    else:
        t += 1
