import colorsys
from datetime import datetime
import thread
import time
import rainbowhat as rh
from random import randint

running = True


def set_running():
    global running
    if running:
        running = False


def days(date_one, date_two):
    date_one = datetime.strptime(date_one, "%Y-%m-%d")
    date_two = datetime.strptime(date_two, "%Y-%m-%d")
    return abs((date_one - date_two).days)


text = "SLEEPS UNTIL XMAS  " + str(days(datetime.today().strftime("%Y-%m-%d"), '2018-12-25'))


def clear():
    # Reset everything
    rh.rainbow.clear()
    rh.rainbow.show()

    rh.display.clear()
    rh.display.show()

    rh.lights.rgb(0, 0, 0)


def scroll(scroll_text):
    while True:
        show = ''
        for letter in scroll_text:
            show = show + letter
            rh.display.clear()
            rh.display.print_str(show)
            rh.display.show()
            time.sleep(0.25)
        time.sleep(2)


def event_handler():
    @rh.touch.A.press()
    def touch_a(channel):
        rh.lights.rgb(1, 0, 0)

    @rh.touch.B.press()
    def touch_b(channel):
        rh.lights.rgb(0, 1, 0)

    @rh.touch.C.press()
    def touch_c(channel):
        rh.lights.rgb(0, 0, 1)
        set_running()


def sequence_all():
    rh.rainbow.set_brightness(0.1)
    for each in range(101):
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb((each / 100.0), 1.0, 1.0)]
        rh.rainbow.set_all(r, g, b)
        rh.rainbow.show()


def sequence_all_ordered(speed):
    rh.rainbow.set_brightness(0.1)
    pixel = 0
    for each in range(101):
        if pixel > 6:
            pixel = 0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb((each / 100.0), 1.0, 1.0)]
        rh.rainbow.set_pixel(pixel, r, g, b)
        rh.rainbow.show()
        time.sleep(speed)
        pixel += 1


def sequence_pixel(speed):
    rh.rainbow.set_brightness(0.1)
    pixel = 0
    for each in range(101):
        if pixel > 6:
            pixel = 0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb((each / 100.0), 1.0, 1.0)]
        rh.rainbow.set_pixel(pixel, r, g, b)
        rh.rainbow.show()
        time.sleep(speed)
        pixel += 1


def sequence_pixel_random(speed):
    rh.rainbow.set_brightness(0.1)
    for each in range(101):
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb((each / 100.0), 1.0, 1.0)]
        rh.rainbow.clear()
        rh.rainbow.set_pixel((randint(0, 6)), r, g, b)
        rh.rainbow.show()
        time.sleep(speed)


def temperature():
    return rh.weather.temperature()


def pressure():
    return rh.weather.pressure()


try:
    while running:
        clear()

        thread.start_new_thread(scroll, (text,))
        thread.start_new_thread(event_handler, ())

        while True:
            # blink(0.1)
            sequence_pixel_random(0.25)
except Exception as exception:
    print(exception)
finally:
    clear()
