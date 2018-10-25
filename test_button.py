#button test
import RPi.GPIO as GPIO

#setting up the pin
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

#configure pin
button = 27
dc = 95 # duty cycle (0-100) for PWM pin
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

input_state = GPIO.input(button)
#print(input_state) #1 not pressed, 0 is pressed

#if input_state == 1:
#	print('button is not pressed')
#else: print ('button is pressed')

while 1==1:
	input_state = GPIO.input(button)
	if input_state == False:
		print('button is pressed')
	
	

#while True:
#    input_state = GPIO.input(button)
#    if input_state == False:
#        print('Button Pressed, led is on!')
