import microcontroller
class Thermometer:
    """Thermometer class allows user to read from the temperature sensor
    on the Adafruit CLUE board
    """

    def getTempterature():
        """getTempterature returns the current temperature from the on
        board microcontroller
        """
        return microcontroller.cpu.temperature