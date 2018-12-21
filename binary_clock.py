from time import time as time

from rainbowhat import rainbow as rainbow
from rainbowhat import display as display

class BinaryClock:
    def __init__(self):
        self.time = time()

    def __str__(self):
        return 'Time is ' + self.time

clock = BinaryClock()
print clock