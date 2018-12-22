from datetime import datetime
import thread
import time

import rainbowhat as rh

from rainbow import Rainbow

scroll_true = True


def days(date_one, date_two):
    date_one = datetime.strptime(date_one, "%Y-%m-%d")
    date_two = datetime.strptime(date_two, "%Y-%m-%d")
    return abs((date_one - date_two).days)


text = "SLEEPS UNTIL XMAS  " + str(days(datetime.today().strftime("%Y-%m-%d"), '2018-12-25'))
rainbow_speed = 0.25


def clear():
    # Reset everything
    rh.rainbow.clear()
    rh.rainbow.show()

    rh.display.clear()
    rh.display.show()

    rh.lights.rgb(0, 0, 0)


def scroll(scroll_text):
    while scroll_true:
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
        global rainbow_speed

        if rainbow_speed >= 0.25:
            rainbow_speed = rainbow_speed - 0.25
        rh.lights.rgb(1, 0, 0)
        print(str(channel) + ' ' + str(rainbow_speed))
        rh.lights.rgb(0, 0, 0)

    @rh.touch.B.press()
    def touch_b(channel):
        global rainbow_speed

        rainbow_speed = rainbow_speed + 0.25
        rh.lights.rgb(0, 1, 0)
        print(str(channel) + ' ' + str(rainbow_speed))
        rh.lights.rgb(0, 0, 0)

    @rh.touch.C.press()
    def touch_c(channel):
        rh.lights.rgb(0, 0, 1)
        print(str(channel) + ' ' + str(rainbow_speed))
        global scroll_true
        scroll_true = False


def temperature():
    return rh.weather.temperature()


def pressure():
    return rh.weather.pressure()


try:
    flashing_lights = Rainbow()
    clear()

    thread.start_new_thread(scroll, (text,))
    thread.start_new_thread(event_handler, ())

    while True:
        flashing_lights.start()
except Exception as exception:
    print(exception)
finally:
    clear()
