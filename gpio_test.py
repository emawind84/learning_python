#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import atexit

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

def app():
    while True:
        if GPIO.input(26) == GPIO.HIGH:
            print('BCM26 went high!')
            GPIO.output(26, not GPIO.input(26))
    time.sleep(2)

def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)

app()