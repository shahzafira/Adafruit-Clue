import time
import board
from analogio import AnalogIn

analog_iin = AnalogIn(board.A1)

def get_voltage(pin):
    retunr (pin.value * 3.3) / 65536

while True:
    print((get_voltage(analog_in),))
    time.sleep(0.1)