import ledsetting

r = 0
b = 0
g = 255


def staticcolor(k=1, i=0):
        while i < ledsetting.MaxLvl:
                while k < ledsetting.led_count:
                        if k=1 or k=3:
                                ledsetting.led_on(i, k, r, g, b)
                                ledsetting.led_on(i, k+1, r, g, b)
                                ledsetting.led_on(i, k+2, r, g, b)
                                ledsetting.led_on(i, k+3, r, g, b)
                                k += 1
                        else:
                                ledsetting.led_on(i, k, r, g, b)
                                ledsetting.led_on(i, k+1, r, g, b)
                                ledsetting.led_on(i, k+2, r, g, b)
                        k += 7
                i += 1