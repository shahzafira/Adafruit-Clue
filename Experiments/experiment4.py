# code for experiment 4
# experiment 4 keeps a constant red light at the highest intensity
# also maintains the moisture level at 0.5v (out of 3v)

from adafruit_clue import clue
import rtc
import time
import board
import neopixel
from analogio import AnalogIn
import digitalio
import microcontroller

# Configure the setup

# NeoPixel setup
PIXEL_PIN = board.D8  # NeoPixel pin
ORDER = neopixel.GRB  # pixel color channel order
COLOR = (255, 0, 0) # red light
CLEAR = (0, 0, 0)  # off light

# Create the NeoPixel object
pixel = neopixel.NeoPixel(PIXEL_PIN, 8, pixel_order=ORDER)

# moisture sensor setup
MOISTURE_LEVEL = 0.5
analog_in = AnalogIn(board.A2)

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

# water pump setup
motor_pin = digitalio.DigitalInOut(board.MISO)
motor_pin.direction = digitalio.Direction.OUTPUT

# date time setup
r = rtc.RTC()
r.datetime = time.struct_time((2022, 1, 1, 0, 0, 0, 0, 0, 0))


# main body

# csv columns day, time, temp, moisture_level, is_water, moisture_after

for light in range(3, 8):
    pixel[light] = COLOR

try:
    with open("/experiment4.csv", "a") as ex:
        while True:
            curr_dt = r.datetime
            curr_t = "{0}:{1}".format(curr_dt.tm_hour, curr_dt.tm_min)
            temp = microcontroller.cpu.temperature
            bef_moist = get_voltage(analog_in)
            is_water = False
            curr_moist = bef_moist

            if curr_moist < MOISTURE_LEVEL:
                is_water = True
                motor_pin.value = True
                time.sleep(0.5)
                motor_pin.value = False
                curr_moist = get_voltage(analog_in)
                
            after_moist = get_voltage(analog_in)
            curr_status = "{day}, {t}, {temp}, {b_moist}, {is_water}, {a_moist}\n".format(
                day = curr_dt.tm_mday, t = curr_t,
                temp = temp, b_moist = bef_moist,
                is_water = is_water, a_moist = after_moist)
            ex.write(curr_status)
            print(curr_status)
            ex.flush()

            # sleep for an hour
            curr_hour = curr_dt.tm_hour
            if curr_hour == 23:
                next_hour = 0
            else:
                next_hour = curr_hour + 1

            while r.datetime.tm_hour != next_hour:
                time.sleep(1)

except OSError as e:
    if e.args[0] == 28:
        t = r.datetime
        print("Storage is full {0}".format(t))
    else:
        print(e)



