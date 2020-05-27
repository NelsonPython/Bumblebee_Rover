<h1>motors.py</h1>

It is easier to troubleshoot the motors if you color code the wires that connect them to the motor controller 
Describing your configuration inside the script doesn't affect driving performance and it is convenient

Motor 1:  yellow ground wire front driverside
Enable = 5
Postive = 24
Negative = 27

Motor 2: green ground wire rear driverside
Enable = 17
Postive = 6
Negative = 22

Motor 3: orange ground wire front passenger
Enable = 12
Positive = 23
Negative = 16

Motor 4: blue ground wire rear passenger
Enable = 25
Positive = 13
Negative = 18
'''

import RPi.GPIO as GPIO
import time
from time import sleep

def setupGPIO(gnd,vcc,enable):
        GPIO.setup(gnd,GPIO.OUT)
        GPIO.setup(vcc,GPIO.OUT)
        GPIO.setup(enable,GPIO.OUT)

def forward(gnd,vcc,enable):
        GPIO.output(gnd,GPIO.HIGH)
        GPIO.output(vcc,GPIO.LOW)
        GPIO.output(enable,GPIO.HIGH)

def backward(gnd,vcc,enable):
        GPIO.output(gnd,GPIO.LOW)
        GPIO.output(vcc,GPIO.HIGH)
        GPIO.output(enable,GPIO.HIGH)

def stop(e1, e2, e3, e4):
        ''' set enable to low to stop '''
        GPIO.output(e1,GPIO.LOW)
        GPIO.output(e2,GPIO.LOW)
        GPIO.output(e3,GPIO.LOW)
        GPIO.output(e4,GPIO.LOW)
        sleep(0.05)

def goForward(forwardTime):
        forward(27,24,5)        # motor 1
        forward(22,6,17)        # motor 2
        forward(23,16,12)       # motor 3
        forward(18,13,25)       # motor 4
        sleep(forwardTime)

def IsFollowingLine(driverLine,passengerLine):
        ''' check the color reported by the black (0) and white (1) sensor
        '''
        # if both line followers are seeing white
        if GPIO.input(driverLine) == 1 and GPIO.input(passengerLine) == 1:
                return True
        else:
                return False

def SeekLine(driverLine,passengerLine):
    turnTime = 0.005
    numTries = 1
    maxTries = 200

    startTime = time.time()
    while numTries <= maxTries:
        # if driver is seeing black and passenger is seeing white, turn left
        if (GPIO.input(driverLine) == 1) and (GPIO.input(passengerLine) == 0):
            #print("seeking left", numTries)
            forward(27,24,5)         # motor 1
            forward(22,6,17)         # motor 2
            backward(23,16,12)       # motor 3
            backward(18,13,25)       # motor 4

        elif (GPIO.input(driverLine) == 0) and (GPIO.input(passengerLine) == 1):
            #print("seeking right ", numTries)
            backward(27,24,5)       # motor 1
            backward(22,6,17)       # motor 2
            forward(23,16,12)       # motor 3
            forward(18,13,25)       # motor 4
        sleep(turnTime)

        goForward(0.0005)

        if IsFollowingLine(driverLine,passengerLine):
                return True

        stopTime = time.time()
        numTries+=1
        if numTries > maxTries:
                print("I started seeking at: ", startTime, " and stopped at: ", stopTime)
                print("I looked for: ", stopTime-startTime, " seconds")
                return False

if __name__ == '__main__':
        print("motors.py")
