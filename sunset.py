import wiringpi
import time


io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
io.pinMode(1,io.PWM_OUTPUT)
io.pwmWrite(1,0)



value = 1023 #how bright the LED is
increment = 1 #how fast to fade up

while value >= 0:
        io.pwmWrite(1,value) #write LED brightness
        value -= increment #increment it
        time.sleep(2.63) #pause for 2.3 s for 45 min sunrise



