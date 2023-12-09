# pip install RPi.GPIO

import RPi.GPIO as GPIO
import time

# Define the GPIO pins
PUL = 9  # Pin 9 for pulse (PUL)
DIR = 8  # Pin 8 for direction (DIR)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)

# Loop for stepper motor control
try:
    while True:
        # Set direction
        GPIO.output(DIR, GPIO.HIGH)  # Set high level direction

        # Rotate 400 steps in one direction
        for x in range(400):
            GPIO.output(PUL, GPIO.HIGH)  # Output high
            time.sleep(0.0005)  # Set rotation speed
            GPIO.output(PUL, GPIO.LOW)  # Output low
            time.sleep(0.0005)  # Set rotation speed

        time.sleep(1)  # Pause for 1 second

        # Set opposite direction
        GPIO.output(DIR, GPIO.LOW)  # Set low level direction

        # Rotate 400 steps in opposite direction
        for x in range(400):
            GPIO.output(PUL, GPIO.HIGH)  # Output high
            time.sleep(0.0005)  # Set rotation speed
            GPIO.output(PUL, GPIO.LOW)  # Output low
            time.sleep(0.0005)  # Set rotation speed

        time.sleep(1)  # Pause for 1 second

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on keyboard interrupt