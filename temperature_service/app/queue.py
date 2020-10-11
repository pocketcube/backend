from app import mqtt
from app import socketio

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(data)
    socketio.emit('mqtt_message', data=data)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('#')
    print('subscribed')