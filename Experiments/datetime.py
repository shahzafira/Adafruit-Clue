# Prints the day (start to end of experiment) and time in h:m:s format
# when button A is pressed

import rtc
import time

from adafruit_clue import clue

# date time setup
r = rtc.RTC()
r.datetime = time.struct_time((2022, 1, 1, 0, 0, 0, 0, 0, 0))

while True:
    if clue.button_a:
        curr = r.datetime
        print("{0}, {1}:{2}:{3}\n".format(curr.tm_mday, curr.tm_hour, curr.tm_min, curr.tm_sec))