import ledsetting
import time

BrightPar = 10
r = 0
b = 0
g = 25.5
char = 2
number = 1


def staticcolor(char, number):
        k = 0
        leftside = 1 + char*7
        rightside = 1 + char*7 + 3
        while k < 42:
                p = leftside - 42 + k
                a = rightside + 42 - k
                if 0 <= p < leftside:
                        if rightside < a < 42:
                                ledsetting.led_on(0, p, r * BrightPar, g * BrightPar, b * BrightPar)
                                ledsetting.led_on(0, a, r * BrightPar, g * BrightPar, b * BrightPar)
                                time.sleep(0.1)
                                ledsetting.led_on(0, p, 0, 0, 0)
                                ledsetting.led_on(0, a, 0, 0, 0)
                        else:
                                ledsetting.led_on(0, p, r * BrightPar, g * BrightPar, b * BrightPar)
                                time.sleep(0.1)
                                ledsetting.led_on(0, p, 0, 0, 0)
                elif rightside < a < 42:
                        ledsetting.led_on(0, a, r * BrightPar, g * BrightPar, b * BrightPar)
                        time.sleep(0.2)
                        ledsetting.led_on(0, a, 0, 0, 0)
                k += 1
        ledsetting.led_on(0, leftside, r * BrightPar, g * BrightPar, b * BrightPar)
        ledsetting.led_on(0, leftside + 1, r * BrightPar, g * BrightPar, b * BrightPar)
        ledsetting.led_on(0, leftside + 2, r * BrightPar, g * BrightPar, b * BrightPar)