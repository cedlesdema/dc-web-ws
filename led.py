import RPi.GPIO as GPIO
import time


class Led():
    def __init__(self, broche):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.broche = broche

        GPIO.setup(broche, GPIO.OUT)

    def on(self):
        GPIO.output(self.broche, GPIO.HIGH)

    def off(self):
        GPIO.output(self.broche, GPIO.LOW)

    def blink(self):
        for i in range(0, 1):
            GPIO.output(self.broche, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(self.broche, GPIO.LOW)
            time.sleep(0.1)
