import ledsetting

r = 0
b = 0
g = 0


def rainbow():
        color = 0
        j = 1
        i = 0
        while j == 1:
                while i < ledsetting.led_count:
                        r, g, b = colorwheel(color)
                        ledsetting.led_on(1, i, r, g, b)
                        i += 1
        color += 5
        if color >= 1531:
                color = 0


def colorwheel(color):
        if color <= 255: # красный макс, зелёный растёт
                r = 255
                g = color
                b = 0
                return r, g, b
        elif color > 255 & color <= 510: # зелёный макс, падает красный
                r = 510 - color
                g = 255
                b = 0
                return r, g, b
        elif color > 510 & color <= 765: # зелёный макс, растёт синий
                r = 0
                g = 255
                b = color - 510
                return r, g, b
        elif color > 765 & color <= 1020: # синий макс, падает зелёный
                r = 0
                g = 1020 - color
                b = 255
                return r, g, b
        elif color > 1020 & color <= 1275: # синий макс, растёт красный
                r = color - 1020
                g = 0
                b = 255
                return r, g, b
        elif color > 1275 & color <= 1530: # красный макс, падает синий
                r = 255
                g = 0
                b = 1530 - color
                return r, g, b