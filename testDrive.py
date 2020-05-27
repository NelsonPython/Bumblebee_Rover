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
