#!/usr/bin/env python
import pika
import json
from time import sleep
import random

credentials = pika.PlainCredentials('user', 'user')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()

while True:
    temp = {'temp': round(random.uniform(20.1, 21.3), 2)}

    print(temp) 
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.temperature',
        body=json.dumps(temp)
    )
    sleep(.1)
    
    print(oxygen)
    oxygen = {'oxygen': '89'}
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.oxygen',
        body=json.dumps(oxygen)
    )
    sleep(.3)

    print(gps)
    gps = { 'lat': '-20.0000','lon': '-20.0000' }
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.gps',
        body=json.dumps(gps)
    )
    sleep(.4)
    
    print(pressure)
    pressure = { 'pressure': '30' }
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.pressure',
        body=json.dumps(pressure)
    )
    sleep(.4)

connection.close()
