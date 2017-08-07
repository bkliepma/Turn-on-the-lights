'''

Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson

Modified by Rui Santos
Complete project details: http://randomnerdtutorials.com

Updated by BK Liepmann

'''
#!/usr/bin/env python
import RPi.GPIO as GPIO
import subprocess
from subprocess import Popen
from flask import Flask, render_template, request
import time
#import sunrise
#import sunset

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes.  
GPIO.setup(23, GPIO.OUT)  # set GPIO 25 as an output. You can use any GPIO port
io = GPIO.PWM(23, 100)    # create an object p for PWM on port 23 at 1024 Hertz  
                        # you can have more than one of these, but they need  
                        # different names for each port   
                        # e.g. p1, p2, motor, servo1 etc.
increment = 1 #how fast to fade up


# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   23 : {'name' : 'GPIO 23', 'state' : GPIO.LOW},
   #24 : {'name' : 'GPIO 24', 'state' : GPIO.LOW}
   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:		
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      #GO GET THE LIGHT LEVEL
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      #GO GET THE LIGHT LEVEL
      # Set the pin high:
      GPIO.output(changePin, GPIO.LOW)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " off."
   if action == "sunrise":   
      Popen('python sunrise.py')
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "sunset":
      Popen('python sunrise.py')
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

