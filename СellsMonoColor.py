import ledsetting
import time

BrightPar = 10
r = 0
b = 0
g = 25.5


def staticcolor(k=1, i=0):
        while i < ledsetting.MaxLvl:
                while k < ledsetting.led_count:
                        if k==1 or k==37:
                                ledsetting.led_on(i, k, r*BrightPar, g*BrightPar, b*BrightPar)
                                ledsetting.led_on(i, k+1, r*BrightPar, g*BrightPar, b*BrightPar)
                                ledsetting.led_on(i, k+2, r*BrightPar, g*BrightPar, b*BrightPar)
                                ledsetting.led_on(i, k+3, r*BrightPar, g*BrightPar, b*BrightPar)
                                k += 1
                        else:
                                ledsetting.led_on(i, k, r*BrightPar, g*BrightPar, b*BrightPar)
                                ledsetting.led_on(i, k+1, r*BrightPar, g*BrightPar, b*BrightPar)
                                ledsetting.led_on(i, k+2, r*BrightPar, g*BrightPar, b*BrightPar)
                        k += 7
                i += 1
                k = 1


def pulsecoloron(k=1, i=0):
        while i < ledsetting.MaxLvl:
                BrightPar = 0
                while BrightPar <= 10:
                        while k < ledsetting.led_count:
                                if k==1 or k==37:
                                        ledsetting.led_on(i, k, r*BrightPar, g*BrightPar, b*BrightPar)
                                        ledsetting.led_on(i, k+1, r*BrightPar, g*BrightPar, b*BrightPar)
                                        ledsetting.led_on(i, k+2, r*BrightPar, g*BrightPar, b*BrightPar)
                                        ledsetting.led_on(i, k+3, r*BrightPar, g*BrightPar, b*BrightPar)
                                        k += 1
                                else:
                                        ledsetting.led_on(i, k, r*BrightPar, g*BrightPar, b*BrightPar)
                                        ledsetting.led_on(i, k+1, r*BrightPar, g*BrightPar, b*BrightPar)
                                        ledsetting.led_on(i, k+2, r*BrightPar, g*BrightPar, b*BrightPar)
                                k += 7

                        k = 1
                        time.sleep(0.0001)
                        BrightPar += 1
                i += 1


def pulsecoloroff(k=1, i=0):
        while i < ledsetting.MaxLvl:
                BrightPar = 10
                while BrightPar >= 0:
                        while k < ledsetting.led_count:
                                if k == 1 or k == 37:
                                        ledsetting.led_on(i, k, r * BrightPar, g * BrightPar, b * BrightPar)
                                        ledsetting.led_on(i, k + 1, r * BrightPar, g * BrightPar, b * BrightPar)
                                        ledsetting.led_on(i, k + 2, r * BrightPar, g * BrightPar, b * BrightPar)
                                        ledsetting.led_on(i, k + 3, r * BrightPar, g * BrightPar, b * BrightPar)
                                        k += 1
                                else:
                                        ledsetting.led_on(i, k, r * BrightPar, g * BrightPar, b * BrightPar)
                                        ledsetting.led_on(i, k + 1, r * BrightPar, g * BrightPar, b * BrightPar)
                                        ledsetting.led_on(i, k + 2, r * BrightPar, g * BrightPar, b * BrightPar)
                                k += 7

                        k = 1
                        time.sleep(0.0001)
                        BrightPar -= 1
                i += 1