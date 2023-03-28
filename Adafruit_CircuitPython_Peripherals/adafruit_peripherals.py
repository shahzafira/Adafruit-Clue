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
import microcontroller

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/shahzafira/Adafruit_CircuitPython_Peripherals.git"

class Peripherals:

    WHITE = (255, 255, 255)
    OFF = (0, 0, 0)
    COLOURS = (OFF, OFF, OFF, OFF, OFF)

    def __init__(self):
        # LED related initialisation
        self.PIXEL_PIN = board.D8
        self.ORDER = neopixel.GRB
        self.pixel = neopixel.NeoPixel(self.PIXEL_PIN, 8, pixel_order=self.ORDER)
        for light in range(3, 8):
            self.pixel[light] = self.COLOURS[light - 3]
        
        # Moisture sensor related initialisation
        self.analog_in = AnalogIn(board.A2)

        # Motor related initialisation
        self.motor_pin = digitalio.DigitalInOut(board.MISO)
        self.motor_pin.direction = digitalio.Direction.OUTPUT

    def setColourLED(self, p1, p2=None, p3=None, p4=None, p5=None):
        """setcolour Changes the colour of each LED pixel
        If only one value is specified, all pixels use the same value.
        This does not turn on the LEDs

        param p1: 3-tuple in RGB order to change the colour of the first pixel
        param p2: 3-tuple in RGB order to change the colour of the second pixel
        param p3: 3-tuple in RGB order to change the colour of the third pixel
        param p4: 3-tuple in RGB order to change the colour of the fourth pixel
        param p5: 3-tuple in RGB order to change the colour of the fifth pixel
        """
        pixels = (p1, p2, p3, p4, p5)
        if pixels[1] == None:
            COLOURS = (pixels[0], pixels[0], pixels[0], pixels[0], pixels[0])
        else:
            for light in range(0, 5):
                if pixels[light] != None:
                    COLOURS[light] = pixels[light]
                else:
                    COLOURS[light] = self.OFF
        
    def turnOnLED(self, p1, p2=None, p3=None, p4=None, p5=None):
        """turnOnLED turns on the specified LED lights
        If only one parameter is given, then all pixels will do the same

        param p1: boolean value to turn on pixel one
        param p2: boolean value to turn on pixel two, default set to p1
        param p3: boolean value to turn on pixel three, default set to p1
        param p4: boolean value to turn on pixel four, default set to p1
        param p5: boolean value to turn on pixel five, default set to p1
        """
        pixels = (p1, p2, p3, p4, p5)
        if pixels[1] == None:
            for light in range(3, 8):
                self.pixel[light] = self.COLOURS[light - 3]
        else:
            for light in range(3, 8):
                if pixels[light - 3] == True:
                    self.pixel[light] = self.COLOURS[light - 3]

    def turnOffLED(self, p1, p2=None, p3=None, p4=None, p5=None):
        """turnOnLED turns off the specified LED lights
        If only one parameter is given, then all pixels will do the same

        param p1: boolean value to turn off pixel one
        param p2: boolean value to turn off pixel two, default set to p1
        param p3: boolean value to turn off pixel three, default set to p1
        param p4: boolean value to turn off pixel four, default set to p1
        param p5: boolean value to turn off pixel five, default set to p1
        """
        pixels = (p1, p2, p3, p4, p5)
        for light in range(3, 8):
            if pixels[light - 3] == False:
                self.pixel[light] = self.OFF

    def LEDTimer(self, sec):
        """LEDTimer turns on the LEDs for the specified time in seconds
        Uses the colours set with setColourLED
        
        param sec: integer time in seconds"""
        self.turnOnLED(True)
        time.sleep(sec)
        self.turnOffLED(True)

    def getMoistureLevel(self):
        """getMoistureLevel returns the moisture level in Volts
        0-3V
        """
        return (self.analog_in.value * 3.3) / 65536

    def startMotor(self):
        """start turns on the motor to pump the water
        """
        self.motor_pin.value = True

    def stopMotor(self):
        """stop turns off the motor to stop the flow of water
        """
        self.motor_pin.value = False
    
    def motorTimer(self, sec):
        """turns on the motor for a specified time (in seconds)
        
        param time: integer time in seconds"""
        self.motor_pin.value = True
        time.sleep(sec)
        self.motor_pin.value = False

    def getTemperature(self):
        """getTempterature returns the current temperature from the on
        board microcontroller
        """
        return microcontroller.cpu.temperature