from flask import Flask, request, session
from flask_socketio import SocketIO
import logging

app = Flask(__name__)
app.secret_key = '123456'
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

import web.view