from app import mqtt
from app import socketio
from app import db, SensorData
from datetime import datetime

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    sensor_data = SensorData(sensor_name=message.topic, timestamp=datetime.now(), sensor_value=message.payload.decode() )
    db.session.add(sensor_data)
    db.session.commit()
    socketio.emit('mqtt_message', data=data)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('sensor/atmospheric')
    mqtt.subscribe('sensor/gps')
    mqtt.subscribe('sensor/gases')

    print('subscribed')