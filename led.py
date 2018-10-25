import RPi.GPIO as GPIO
import time

#setting up the mode and off the warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin Setup:
pnled1 = 18
pnled2 = 27
pnbutton = 17
GPIO.setup(pnled1,GPIO.OUT)
GPIO.setup(pnled2,GPIO.OUT)
GPIO.setup(pnbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#this lines to toggle the pin
#print ("LED on")
#GPIO.output(pnled1,GPIO.HIGH)
#time.sleep(1)
#print ("LED off")
#GPIO.output(pnled1,GPIO.LOW)

while True:
    input_state = GPIO.input(pnbutton)
    if input_state == False:
        print('Button Pressed, led is on!')
        GPIO.output(pnled1, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(pnled1, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(pnled2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(pnled2, GPIO.LOW)        

