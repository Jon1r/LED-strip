import board
import neopixel

led_count = 42

pixels = neopixel.NeoPixel(board.D18, led_count)
p = 0


def led_on(l, n, r, g, b):
    p = l*42+n
    pixels[p] = (r, g, b)


