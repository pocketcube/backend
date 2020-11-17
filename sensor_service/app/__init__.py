from flask import Flask
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
from flask_sqlalchemy import SQLAlchemy
import os

db_path = os.path.join(os.path.dirname(__file__), 'app.db')
db_uri = 'sqlite:///{}'.format(db_path)

app = Flask(__name__)
app.config['SECRET'] = 'my secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'rabbit'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 100
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_CLIENT_ID'] = 'user'
app.config['MQTT_USERNAME'] = 'user'
app.config['MQTT_PASSWORD'] = 'user'

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

database = SQLAlchemy(app)
mqtt = Mqtt(app)
socketio = SocketIO(app)

'''
       import inner packages here to avoid 
       circular reference
'''
from app import api
from app import queue
from app import db