from rainbowhat import rainbow as rainbow
from colorsys import hsv_to_rgb
from time import sleep
from random import randint

DELAY_STEP = 0.01  # 10ms interval for stepping the lights
DELAY_MAX = 2  # 2000ms maximum delay
DELAY_MIN = 0.01  # 10ms minimum delay


class Rainbow:
    def __init__(self, speed=0.25, colour=0, sequence='all'):
        self.speed = speed  # Default delay in seconds on each iteration
        self.colour = colour  # RGB value from 1-255, 0 is HSV cycled colour
        self.sequence = sequence  # String: random (one LED at random)
        self.running = True
        #         single (one LED after the other turning the last off)
        #         fill   (one LED after the other leaving the last on)
        #         all    (all LED on)

    @staticmethod
    def blank():
        # Clears the LED and displays it cleared
        rainbow.clear()
        rainbow.show()

    def start(self):
        self.blank()
        try:
            if self.sequence == 'random':
                for each in range(101):
                    r, g, b = [int(c * 255) for c in hsv_to_rgb((each / 100.0), 1.0, 1.0)]
                    rainbow.clear()
                    rainbow.set_pixel((randint(0, 6)), r, g, b)
                    rainbow.show()
                    sleep(self.speed)
            elif self.sequence == 'single':
                pixel = 0
                for each in range(101):
                    if pixel > 6:
                        pixel = 0
                    r, g, b = [int(c * 255) for c in hsv_to_rgb((each / 100.0), 1.0, 1.0)]
                    rainbow.clear()
                    rainbow.show()
                    rainbow.set_pixel(pixel, r, g, b)
                    rainbow.show()
                    sleep(self.speed)
                    pixel += 1
            elif self.sequence == 'fill':
                pixel = 0
                for each in range(101):
                    if pixel > 6:
                        pixel = 0
                    r, g, b = [int(c * 255) for c in hsv_to_rgb((each / 100.0), 1.0, 1.0)]
                    rainbow.set_pixel(pixel, r, g, b)
                    rainbow.show()
                    sleep(self.speed)
                    pixel += 1
            else:
                for each in range(101):
                    r, g, b = [int(c * 255) for c in hsv_to_rgb((each / 100.0), 1.0, 1.0)]
                    rainbow.set_all(r, g, b)
                    rainbow.show()
        except Exception as exception:
            print exception
            print "Something went wrong instantiating the type of sequence!"

    def speed_down(self):
        if self.speed <= DELAY_MAX:
            self.speed = self.speed + DELAY_STEP

    def speed_up(self):
        if self.speed >= DELAY_MIN:
            self.speed = self.speed - DELAY_STEP
