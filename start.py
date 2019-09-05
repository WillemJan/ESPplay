import time
from machine import Pin
from neopixel import NeoPixel
from machine import RTC

date_str = '''2019,10,05,06,31,0,0,0'''
datetime = tuple([int(i) for i in date_str.split(',')])
rtc = RTC()
rtc.datetime(datetime) # set a specific date and time
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
    np.write()              # write data to all pixels
    time.sleep(0.004)

    if t == 32:
        t = 0
    else:
        t += 1
