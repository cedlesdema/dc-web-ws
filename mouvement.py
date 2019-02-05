import RPi.GPIO as GPIO
import time
from flask_socketio import SocketIO, send, emit
from led import Led
from buzzer import Buzzer

# //Initialisation de notre GPIO 17 pour recevoir un signal
# //Contrairement à nos LEDs avec lesquelles on envoyait un signal
lightblue = Led(24)
lightred = Led(18)
buzzer = Buzzer(22)

class Movement():
    def __init__(self, broche):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.broche = broche
        GPIO.setup(broche, GPIO.IN)

    def movement_loop(self, socketio):
        currentstate = 0
        previousstate = 0
        while True:
            currentstate = GPIO.input(self.broche)
            if currentstate == 1 and previousstate == 0:
                lightblue.off()
                buzzer.on()
                lightred.blink()
                buzzer.on()
                lightred.blink()
                buzzer.on()
                lightred.blink()
                buzzer.on()
                lightred.blink()
                socketio.emit('alert', '1', Broadcast=True)
                previousstate = 1
            elif currentstate == 0 and previousstate == 1:
                lightred.off()
                lightblue.on()
                socketio.emit('alert', '0', Broadcast=True)
                previousstate = 0
            time.sleep(0.01)

