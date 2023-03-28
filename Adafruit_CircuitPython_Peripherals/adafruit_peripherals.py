# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Zafira Shah for KCL Final Year Project
#
# SPDX-License-Identifier: MIT
"""
`adafruit_peripherals`
================================================================================

Controls external components that can be connected to the Kitronik greenhouse kit


* Author(s): Zafira Shah

Implementation Notes
--------------------

**Hardware:**

# * Kitronik environmental board for bbc:microbit: https://resources.kitronik.co.uk/pdf/5697-kitronik-environmental-board-for-bbc-micro-bit-datasheet.pdf


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""

# imports
from adafruit_clue import clue
import board
import neopixel
from analogio import AnalogIn
import digitalio
import time
import rtc
import microcontroller

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/shahzafira/Adafruit_CircuitPython_Peripherals.git"

class Facade:

    WHITE = (255, 255, 255)
    OFF = (0, 0, 0)
    COLOURS = (WHITE, WHITE, WHITE, WHITE)

    def __init__(self):
        # LED related initialisation
        PIXEL_PIN = board.D8
        ORDER = neopixel.GRB
        pixel = neopixel.NeoPixel(PIXEL_PIN, 8, pixel_order=ORDER)
        for light in range(3, 8):
            pixel[light] = OFF
        
        # Moisture sensor related initialisation
        analog_in = AnalogIn(board.A2)

        # Motor related initialisation
        motor_pin = digitalio.DigitalInOut(board.MISO)
        motor_pin.direction = digitalio.Direction.OUTPUT

    def setColourLED(p1, p2=None, p3=None, p4=None):
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

    def LEDTimer(sec):
        """LEDTimer turns on the LEDs for the specified time in seconds
        Uses the colours set with setColourLED
        
        param sec: integer time in seconds"""
        turnOnLED(True)
        time.sleep(sec)
        turnOffLED(True)

    def getMoistureLevel():
        """getMoistureLevel returns the moisture level in Volts
        0-3V
        """
        return (analog_in.value * 3.3) / 65536

    def startMotor():
        """start turns on the motor to pump the water
        """
        motor_pin.value = True

    def stopMotor():
        """stop turns off the motor to stop the flow of water
        """
        motor_pin.value = False
    
    def motorTimer(sec):
        """turns on the motor for a specified time (in seconds)
        
        param time: integer time in seconds"""
        motor_pin.value = True
        time.sleep(sec)
        motor_pin.value = False

    def getTemperature():
        """getTempterature returns the current temperature from the on
        board microcontroller
        """
        return microcontroller.cpu.temperature