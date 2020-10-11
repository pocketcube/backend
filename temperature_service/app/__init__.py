from flask import Flask
from flask_socketio import SocketIO
from flask_mqtt import Mqtt

app = Flask(__name__)
app.config['SECRET'] = 'my secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'rabbit'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 100
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_CLIENT_ID'] = 'test'
app.config['MQTT_USERNAME'] = 'test'
app.config['MQTT_PASSWORD'] = 'test'

mqtt = Mqtt(app)
socketio = SocketIO(app)

'''
       import inner packages here to avoid 
       circular reference
'''
from app import api
from app import queue