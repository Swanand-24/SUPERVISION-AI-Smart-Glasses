import RPi.GPIO as GPIO
import time
import os

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Set pins for ultrasonic sensor
TRIG = 14
ECHO = 18

# Set GPIO direction (TRIG as OUTPUT, ECHO as INPUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Initialize previous command and last warning time
prev_command = ""
last_warning_time = 0

def distance():
    # Trigger pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Measure the duration of the pulse
    start_time = time.time()
    end_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Calculate distance
    duration = end_time - start_time
    distance_cm = duration * 17150
    return distance_cm

# Welcome voice command
os.system('espeak "Obstacle detection is now enabled"')

try:
    start_time = time.time()  # Record the start time
    while time.time() - start_time <= 50:  # Run for 30 seconds
        dist = distance()

        # Check if the distance is under 75cm
        if dist < 75:
            print("Distance:", dist, "cm")

            command = "Stop. Object detected at {} centimeters.".format(int(dist))

            # Check if the new command is different from the previous one
            if command != prev_command:
                current_time = time.time()
                if current_time - last_warning_time >= 5:
                    os.system('espeak "{}"'.format(command))
                    last_warning_time = current_time
                prev_command = command

        time.sleep(0.1)  # Short delay to control loop frequency

except KeyboardInterrupt:
    GPIO.cleanup()
