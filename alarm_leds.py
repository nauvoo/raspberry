import RPi.GPIO as GPIO
from datetime import datetime, timedelta
import time
#using BCM scheme, pin18 is physical pin 6 from right
GPIO.setmode(GPIO.BCM) #setting up the format of counting pins
GPIO.setwarnings(False)

ledPin = 4
butPin = 18

GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sets up state of the button, receiving input data on pin 18
GPIO.setup(ledPin,GPIO.OUT, initial=GPIO.LOW) #set up another pin to send the current above

#setting up time variables
s1 = time.strftime("%H:%M:%S" )#current time
s2 = input('Provide time input in the following format: HH:MM:SS ') # alarm time
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)

try:
    while tdelta != 0:
        time.sleep(1)
        tdelta = tdelta-timedelta(seconds=1)
        print(tdelta.seconds)
    #once condition is not met:
        if tdelta.seconds == 0:
            while GPIO.input(18) == True:  #while button is not pressed, light LEDs
                print(tdelta.seconds)
                GPIO.output(ledPin, GPIO.HIGH) # Turn on
                time.sleep(1) 
                GPIO.output(ledPin, GPIO.LOW) # Turn off
                time.sleep(1) # Sleep for 1 second
            if GPIO.input(18) == False: #if button is pressed, break the loop
                break
except KeyboardInterrupt:
    print('You cancelled the operation.')
#    while True:
#        input_state = GPIO.input(butPin) #need to include it here so while loop checks constantly
#        if GPIO.input(butPin) == False:
#            break
#            print('Button Pressed')
#            GPIO.output(4,GPIO.LOW)
        #when button is pressed