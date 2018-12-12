from datetime import datetime
import thread
import time

import rainbowhat as rh

from rainbow import Rainbow

running = True
rainbow_speed = 0.25  # The delay in seconds between repetitions of the rainbow LED sequence


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
    global rainbow_speed

    @rh.touch.A.press()
    def touch_a(channel):
        rh.lights.rgb(1, 0, 0)
        print(str(channel) + ' ' + str(rainbow_speed))

    @rh.touch.B.press()
    def touch_b(channel):
        rh.lights.rgb(0, 1, 0)
        print(str(channel) + ' ' + str(rainbow_speed))

    @rh.touch.C.press()
    def touch_c(channel):
        rh.lights.rgb(0, 0, 1)
        print(str(channel) + ' ' + str(rainbow_speed))
        set_running()


def temperature():
    return rh.weather.temperature()


def pressure():
    return rh.weather.pressure()


try:
    while running:
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
