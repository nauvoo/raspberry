#link.py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD) possibly for another schema setup
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, True)
GPIO.output(18, False)

GPIO.cleanup()
#time.sleep(1)
#GPIO.output(23, False)
#time.sleep(1)
#GPIO.output(23, True)
#time.sleep(1)
#GPIO.output(23, False)
#setting second pin
#GPIO.setup(21,GPIO.OUT)
#print ("LED on")
#GPIO.output(21,GPIO.HIGH)
#time.sleep(1)
#print ("LED off")
#GPIO.output(21,GPIO.LOW)
