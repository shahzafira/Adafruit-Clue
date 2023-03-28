import LED
import MoistureSensor
import Motor
import Thermometer
class Facade:
    def __init__(self):
        pass

    def setColourLED(p1, p2=None, p3=None, p4=None):
        LED.setColour(p1, p2, p2, p4)
        
    def turnOnLED(p1, p2=None, p3=None, p4=None):
        LED.turnOnLED(p1, p2, p3, p4)

    def turnOffLED(p1, p2=None, p3=None, p4=None):
        LED.turnOffLED(p1, p2, p3, p4)

    def getMoistureLevel():
        MoistureSensor.getMoistureLevel()

    def startMotor():
        Motor.start()

    def stopMotor():
        Motor.stop()
    
    def motorTimer(sec):
        Motor.onForTime(sec)

    def getTemperature():
        Thermometer.getTemperature()