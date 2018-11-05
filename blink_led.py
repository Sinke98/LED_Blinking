import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)
while 1:
   GPIO.output(4, True)
   time.sleep(1)
   GPIO.output(False)
   time.sleep(1)
