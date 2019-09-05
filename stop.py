import machine, time
from machine import Pin
from neopixel import NeoPixel
from machine import RTC

rtc = RTC()
rtc.datetime((2019, 9, 1, 10, 49, 0, 0, 0)) # set a specific date and time
