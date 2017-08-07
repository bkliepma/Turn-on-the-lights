#!/usr/bin/python
import wiringpi 
import time 
import sys
import select

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS) 
io.pinMode(1,io.PWM_OUTPUT) 
io.pwmWrite(1,0) 
value = 0 #how bright the LED is
increment = 1 #how fast to fade up
 
while value < 1024:
	io.pwmWrite(1,value) #write LED brightness
	#print value
       	value += increment #increment it
       	time.sleep(2.63) #pause for 2.3 s for 45 min sunrise #this is not needed with the 2.63 s select above
