import board
import neopixel
class LED:
    """LED class allows users to control the LED lights in the greenhouse
    (neopixel ZIP 5 LED strip lights)
    """
    WHITE = (255, 255, 255)
    OFF = (0, 0, 0)
    COLOURS = (WHITE, WHITE, WHITE, WHITE)

    def __init__(self):
        PIXEL_PIN = board.D8
        ORDER = neopixel.GRB
        pixel = neopixel.NeoPixel(PIXEL_PIN, 8, pixel_order=ORDER)
        for light in range(3, 8):
            pixel[light] = OFF

    def setColour(p1, p2=None, p3=None, p4=None):
        """setcolour Changes the colour of each LED pixel
        If only one value is specified, all pixels use the same value

        param p1: 3-tuple in RGB order to change the colour of the first pixel
        param p2: 3-tuple in RGB order to change the colour of the second pixel
        param p3: 3-tuple in RGB order to change the colour of the third pixel
        param p4: 3-tuple in RGB order to change the colour of the fourth pixel
        """
        if p2 == None:
            COLOURS = (p1, p1, p1, p1)
        else:
            COLOURS = (p1, p2, p3, p4)

    def setIntensity(intensity):
        # set intensity with %
        # divide all rgb values by %
        pass
    
    def turnOnLED(led):
        """turnOnLED turns on the LED lights using the colours from setColour
        Specify which LED to turn on in range 0 - 4 or enter 5 to turn on all

        param led: single number in range 0-4 or 5 for all lights
        """
        if led < 5:
            pixel[led + 3] = COLOURS[led]
        else:
            for light in range(3, 8):
                pixel[light] = COLOURS[light - 3]

    def turnOffLED(led):
        """turnOffLED sets the specified LED lights to 0
        Specify which LED to turn off in range 0 - 4 or enter 5 to turn off all

        param led: single numebr in range 0-4 or 5 for all lights
        """
        if led < 5:
            pixel[led + 3] = OFF
        else:
            for light in range(3, 8):
                pixel[light] = OFF
    
