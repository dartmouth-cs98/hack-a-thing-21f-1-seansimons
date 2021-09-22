import RPi.GPIO as GPIO
import time

yellowPin = 18
bluePin = 23
btnPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(yellowPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(bluePin, GPIO.LOW)
try:
    while 1:
        if GPIO.input(btnPin):
            GPIO.output(yellowPin, GPIO.HIGH)
            GPIO.output(bluePin, GPIO.LOW)
        else:
            GPIO.output(yellowPin, GPIO.LOW)
            GPIO.output(bluePin, GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(bluePin, GPIO.LOW)
            time.sleep(0.075)
except KeyboardInterrupt:
    GPIO.cleanup()
