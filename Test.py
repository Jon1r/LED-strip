import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 30)

y = 1
f = 1
x = 0
while y == 1:
    if f == 1:
        f = 0
        while x <= 20:
            pixels[x] = (255, 0, 0)
            time.sleep(0.5)
            x += 1
    else:
        f = 1
        while x > -1:
            pixels[x] = (0, 255, 0)
            time.sleep(0.5)
            x -= 1

