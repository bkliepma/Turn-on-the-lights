#!/usr/bin/python
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes.  
GPIO.setup(23, GPIO.OUT)  # set GPIO 25 as an output. You can use any GPIO port
io = GPIO.PWM(23, 100)    # create an object p for PWM on port 23 at 1024 Hertz$
                        # you can have more than one of these, but they need  
                        # different names for each port   
                        # e.g. p1, p2, motor, servo1 etc.
f = open("lightLevel","r") #open the universal file to read
value = int(f.read()) #get the value (INT)
io.start(value) #turn the lights on/off if something adjusted them improperly

