import board
import neopixel

led_count = 42
MaxLvl = 3

full_count = led_count*MaxLvl

pixels = neopixel.NeoPixel(board.D18, full_count)
p = 0


def led_on(l, n, r, g, b):
    p = l*42+n
    pixels[p] = (r, g, b)


