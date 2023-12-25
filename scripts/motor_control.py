# pip install RPi.GPIO

import RPi.GPIO as GPIO
import time

# Define the GPIO pins
PUL = 9
DIR = 8

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)

try:
    while True:
        # Set direction
        GPIO.output(DIR, GPIO.HIGH)

        # Rotate 400 steps in one direction
        for x in range(400):
            GPIO.output(PUL, GPIO.HIGH)
            time.sleep(0.0005)
            GPIO.output(PUL, GPIO.LOW)
            time.sleep(0.0005)

        time.sleep(1)

        # Set opposite direction
        GPIO.output(DIR, GPIO.LOW)

        for x in range(400):
            GPIO.output(PUL, GPIO.HIGH)
            time.sleep(0.0005)
            GPIO.output(PUL, GPIO.LOW)
            time.sleep(0.0005)

        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()