import time
import machine
import apa102

# 1M strip with 60 LEDs
strip = apa102.APA102(machine.Pin(14), machine.Pin(13), 37)


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


brightness = 1  # 0 is off, 1 is dim, 31 is max
# Demo 1: RGB RGB RGB
red = 0xff0000
green = red >> 8
blue = red >> 16
for i in range(strip.n):
    colour = red >> (i % 3) * 8
    strip[i] = ((colour & red) >> 16,
                (colour & green) >> 8,
                (colour & blue),
                brightness)
strip.write()

print('demo1 done')

# Demo 2: Show all colours of the rainbow
for i in range(strip.n):
    strip[i] = wheel((i * 256 // strip.n) % 255, brightness)
strip.write()
print('demo2 done')

# Demo 3: Fade all pixels together through rainbow colours,
# offset each pixel
for r in range(5):
    for n in range(256):
        for i in range(strip.n):
            strip[i] = wheel(((i * 256 // strip.n) + n) & 255, brightness)
        strip.write()
    time.sleep_ms(25)
print('demo3 done')


# Demo 4: Same colour, different brightness levels
for b in range(31, -1, -1):
    strip[0] = (255, 153, 0, b)
    strip.write()
    time.sleep_ms(250)

# End: Turn off all the LEDs
strip.fill((0, 0, 0, 0))
strip.write()
print('demo4 done')
