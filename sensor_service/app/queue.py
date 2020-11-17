from app import mqtt
from app import socketio
from app.db import save_data

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    save_data(message.topic, message.payload.decode())
    socketio.emit('mqtt_message', data=data)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('sensor/atmospheric')
    mqtt.subscribe('sensor/gps')
    mqtt.subscribe('sensor/gases')

    print('subscribed')