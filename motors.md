<h1>Test driving Bumblebee AV</h1>

The wires that connect the motor controller to the motors have been color-coded.  Use this guide to check the wiring if any of the wheels do not turn or they turn in the wrong direction

```
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
```


<h3>testDrive.py</h3>


import RPi.GPIO as GPIO
import time
from time import sleep

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

GPIO.setup(gnd,GPIO.OUT)
GPIO.setup(vcc,GPIO.OUT)
GPIO.setup(enable,GPIO.OUT)

forward(0.5)
stop()
backward(0.5)
stop()
