#!/usr/bin/python
# - BOBOF TOILET EXPERIENCE -
#
# Small script to be able to relive the true Bobof Grill MM toilet experience!
# 30 degress celsius, lights flashing, just like a rave party!
#
# Connect a relay to GPIO18 / PIN12 on a Raspberry PI.

import RPi.GPIO as GPIO
import re
import time
import random

def main():
    # Initialize GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    print("GPIO initialized.")
    # DEBUG
    #test_relay()
    # Keep on forever...
    while True:
        flash()

def flash():
    # Randomizing final outcome
    rand_bool = random.getrandbits(1)
    #print "Random number this run is *drumroll* %s" % rand_bool

    # Run the loop 20 times
    for x in range(20):
        # Generate a random number 1-101
        current_value = random.randint(1,101)
        # Generate a random int 0-1
        rand_int = random.randint(0, 1)
        # Send random int to GPIO
        GPIO.output(12, int(rand_int))
        # Take a small break of 0.value seconds
        current_value = "0." + str(current_value)
        time.sleep(float(current_value))

    # When loop is over, lamp should either be lit of off before randomizing again
    GPIO.output(12, int(rand_bool))
    # Let the customer enjoy lit or dark for some seconds.
    rand_int = random.randint(10, 30)
    time.sleep(rand_int)

def test_relay():
    print ("Testing testing (click-click)")
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.10)
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.10)
    GPIO.output(12, GPIO.LOW)

if __name__ == "__main__":
    main()