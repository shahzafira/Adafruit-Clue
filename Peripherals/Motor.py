import digitalio
import board
class Motor:
    """Motor class allows the user to control the motor peripheral
    for the greenhouse
    """
    def __init__(self):
        motor_pin = digitalio.DigitalInOut(board.MISO)
        motor_pin.direction = digitalio.Direction.OUTPUT

    def start():
        """start turns on the motor to pump the water
        """
        motor_pin.value = True

    def stop():
        """stop turns off the motor to stop the flow of water
        """
        motor_pin.value = False