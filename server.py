from flask import Flask
from flask_socketio import SocketIO, send, emit
from flask import render_template
import time
import threading
from mouvement import Movement

app = Flask(__name__)

socketio = SocketIO(app)
@app.route("/")
def index():
    return render_template('index.html')


# def message_loop():
#     while True:
#         message = input('Votre message ?')
#         socketio.emit('alert', message, Broadcast=True)

# Vue que notre méthode pour lire nos message est une boucle infinie
# Elle bloquerait notre serveur. Qui ne pourrait répondre à aucune requête.
# Ici nous créons un Thread qui va permettre à notre fonction de se lancer
# en parallèle du serveur.




mouvement = Movement(17)
read_mouvement = threading.Thread(target=mouvement.movement_loop,args=(socketio,))
read_mouvement.start()
