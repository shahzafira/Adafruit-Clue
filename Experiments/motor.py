from adafruit_clue import clue
import board
import digitalio

led_pin = digitalio.DigitalInOut(board.MISO)
led_pin.direction = digitalio.Direction.OUTPUT

while True:
    if clue.button_a or clue.button_b:
        led_pin.value = True
    else:
        led_pin.value = False