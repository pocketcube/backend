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
    
    # Dados de temperatura
    temp = {'temp': round(random.uniform(20.1, 21.3), 2)}
    print(temp) 
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.temperature',
        body=json.dumps(temp)
    )
    sleep(.1)
    
    # Dados de oxigênio
    oxygen = {'oxygen': '89'}
    print(oxygen)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.oxygen',
        body=json.dumps(oxygen)
    )
    sleep(.3)

    # Dados de GPS
    gps = { 'lat': '-20.0000','lon': '-20.0000' }
    print(gps)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.gps',
        body=json.dumps(gps)
    )
    sleep(.4)
    
    # Dados de pressão
    pressure = { 'pressure': '30' }
    print(pressure)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.pressure',
        body=json.dumps(pressure)
    )
    sleep(.4)

connection.close()
