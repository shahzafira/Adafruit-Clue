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
        If only one value is specified, all pixels use the same value.
        This does not turn on the LEDs

        param p1: 3-tuple in RGB order to change the colour of the first pixel
        param p2: 3-tuple in RGB order to change the colour of the second pixel
        param p3: 3-tuple in RGB order to change the colour of the third pixel
        param p4: 3-tuple in RGB order to change the colour of the fourth pixel
        """
        if p2 == None:
            COLOURS = (p1, p1, p1, p1)
        else:
            COLOURS = (p1, p2, p3, p4)

    def turnOnLED(p1, p2=None, p3=None, p4=None):
        """turnOnLED turns on the specified LED lights
        If only one parameter is given, then all pixels will do the same

        param p1: boolean value to turn on pixel one
        param p2: boolean value to turn on pixel two, default set to p1
        param p3: boolean value to turn on pixel three, default set to p1
        param p4: boolean value to turn on pixel four, default set to p1
        """
        pixels = (p1, p2, p3, p4)
        for light in range(3, 8):
            if pixels[light] == True:
                pixel[light] = COLOURS[light - 3]

    def turnOffLED(p1, p2=None, p3=None, p4=None):
        """turnOnLED turns off the specified LED lights
        If only one parameter is given, then all pixels will do the same

        param p1: boolean value to turn off pixel one
        param p2: boolean value to turn off pixel two, default set to p1
        param p3: boolean value to turn off pixel three, default set to p1
        param p4: boolean value to turn off pixel four, default set to p1
        """
        pixels = (p1, p2, p3, p4)
        for light in range(3, 8):
            if pixels[light] == False:
                pixel[light] = OFF
    
