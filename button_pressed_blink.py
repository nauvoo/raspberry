import RPi.GPIO as GPIO
import time

# Pin Definitons:
#using BCM scheme, pin18 is physical pin 6 from right
GPIO.setmode(GPIO.BCM) #setting up the format of counting pins
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sets up state of the button, receiving input data on pin 18
GPIO.setup(4,GPIO.OUT)
#set up another pin to send the current above
#GPIO04 is forth pin from the left side

while True:
    input_state = GPIO.input(18) #input state is True, button not pressed
    if input_state == False:
        print('Button Pressed')
        GPIO.output(4,GPIO.HIGH)
        time.sleep(0.2)
    else:
        GPIO.output(4,GPIO.LOW)