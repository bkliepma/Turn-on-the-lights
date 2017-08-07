#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes.  
GPIO.setup(23, GPIO.OUT)  # set GPIO 25 as an output. You can use any GPIO port
io = GPIO.PWM(23, 100)    # create an object p for PWM on port 23 at 1024 Hertz$
                        # you can have more than one of these, but they need  
                        # different names for each port   
                        # e.g. p1, p2, motor, servo1 etc.
increment = 1 #how fast to fade up
f = open("lightLevel","r") #open the universal file to read
value = int(f.read()) #get the value (INT)
	
while value > 0:
	f = open("lightLevel","r") #open the universal file to read
	value = int(f.read()) #get the value (INT)
        io.start(value) #write LED brightness AS A PERCENTAGE OF DUTY CYCLE
	f.close() #close the file
        value -= increment #increment it
	f = open("lightLevel", "w")  #open the file to write (overwriting the old value)
	f.write(str(value)) #write the value as a string to the file
	f.close()
        time.sleep(.1) #pause for 2.3 s for 45 min sunrise 
        print (value)
GPIO.cleanup()
