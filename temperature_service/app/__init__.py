import eventlet
from flask import Flask
from flask_socketio import SocketIO
from flask_mqtt import Mqtt

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET'] = 'my secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'localhost'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_CLIENT_ID'] = ''


app = Flask(__name__)

mqtt = Mqtt(app)
socketio = SocketIO(app)

'''
       import inner packages here to avoid 
       circular reference
'''
from app import api
from app import queue