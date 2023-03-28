from analogio import AnalogIn
import board
class MoistureSensor:
    def __init__(self):
        analog_in = AnalogIn(board.A2)

    def getMoistureLevel():
        """getMoistureLevel returns the moisture level in Volts
        0-3V
        """
        return (analog_in.value * 3.3) / 65536