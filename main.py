from datetime import datetime
from time import sleep

import thread

import rainbowhat as rh

from rainbow import Rainbow


def days(date_one, date_two):
    date_one = datetime.strptime(date_one, "%Y-%m-%d")
    date_two = datetime.strptime(date_two, "%Y-%m-%d")
    return abs((date_one - date_two).days)


text = str(days(datetime.today().strftime("%Y-%m-%d"), '2018-12-25')) + " SLEEPS UNTIL XMAS    "


def clear():
    # Reset everything
    rh.rainbow.clear()
    rh.rainbow.show()

    rh.display.clear()
    rh.display.show()

    rh.lights.rgb(0, 0, 0)


def scroll(scroll_text):
    show = ''
    while True:
        for letter in scroll_text:
            show = show + letter
            rh.display.clear()
            rh.display.print_str(show)
            rh.display.show()
            sleep(0.25)


def event_handler():
    @rh.touch.A.press()
    def touch_a(channel):
        rh.lights.rgb(1, 0, 0)
        flashing_lights.speed_down()
        print(str(channel) + " " + str(flashing_lights.speed))
        sleep(0.5)
        rh.lights.rgb(0, 0, 0)

    @rh.touch.B.press()
    def touch_b(channel):
        rh.lights.rgb(0, 1, 0)
        flashing_lights.speed_up()
        print(str(channel) + " " + str(flashing_lights.speed))
        sleep(0.5)
        rh.lights.rgb(0, 0, 0)

    @rh.touch.C.press()
    def touch_c(channel):
        rh.lights.rgb(0, 0, 1)
        print(str(channel))
        sleep(0.5)
        rh.lights.rgb(0, 0, 0)


def temperature():
    return rh.weather.temperature()


def pressure():
    return rh.weather.pressure()


try:
    flashing_lights = Rainbow(sequence='single')
    clear()

    thread.start_new_thread(scroll, (text,))
    thread.start_new_thread(event_handler, ())

    while True:
        flashing_lights.start()
except Exception as exception:
    print(exception)
finally:
    clear()
