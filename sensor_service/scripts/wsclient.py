import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.on('mqtt_message')
def on_message(data):
    print('message received with ', data)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')
sio.wait()
