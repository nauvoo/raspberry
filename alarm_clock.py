#command to set up the audio output on a terminal
#amixer cset numid=3 1 - for audio jack
import RPi.GPIO as GPIO
import time
import pygame
import os

# Pin Definitons:
button = 27
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#to set up for input when button is pressed
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
input_state = GPIO.input(button)

#will play for x seconds duration the song, the value could be a variable

x = 0





#try:
#	if input_state == True: #button is not pressed
#		os.system('timeout 2 cvlc /home/pi/Downloads/alarm_song.mp3')
#	else: 
#		os.system('cvlc /home/pi/Downloads/alarm_song.mp3')
#except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
#   GPIO.cleanup() # cleanup all GPIO			
		
			
			
#	input_state == True: #if button is not pressed:
#		os.system('cvlc /home/pi/Downloads/alarm_song.mp3')
#	else input_state == False: #if button is pressed
#		os.system('timeout 0.2 cvlc /home/pi/Downloads/alarm_song.mp3' )
#except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
 #   GPIO.cleanup() # cleanup all GPIO
