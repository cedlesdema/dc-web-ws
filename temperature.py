# Imports
import os
import glob
import time
from flask_socketio import SocketIO, send, emit

class TemperatureSensor:
    def __init__(self):
        # Intialisation des broches
        os.system('modprobe w1-gpio')  # Allume le module 1wire
        os.system('modprobe w1-therm')  # Allume le module Temperature

        # Chemin du fichier contenant la température (remplacer par votre valeur trouvée précéde$
        self.device_file = '/sys/bus/w1/devices/28-01131a3de1fd/w1_slave'

    # Une fonction qui lit dans le fichier température
    def read_temp_raw(self):
        f = open(self.device_file, 'r')  # Ouvre le dichier
        lines = f.readlines() # Returns the text
        f.close()
        return lines

    # Lis la temperature
    def read_temp_c(self):
        lines = self.read_temp_raw()  # Lit le fichier de température
        # Tant que la première ligne ne vaut pas 'YES', on attend 0,2s
        # On relis ensuite le fichier
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
            # On cherche le '=' dans la seconde ligne du fichier
        equals_pos = lines[1].find('t=')
        # Si le '=' est trouvé, on converti ce qu'il y a après le '=' en degrées celcius
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c

    def read_temp_f(self):
        fahrenheit = (self.read_temp_c()*1.8)+32
        return fahrenheit

    def infinite_temperature(self, socketio):
        sensor = TemperatureSensor()
        while True:
            socketio.emit('alert', 'la temperature est de : '+ str(sensor.read_temp_f()) +'degré Fahrenheit', Broadcast=True)
            socketio.emit('alert', 'la temperature est de : '+ str(sensor.read_temp_c()) +'degré Celsius', Broadcast=True)
            time.sleep(1)
