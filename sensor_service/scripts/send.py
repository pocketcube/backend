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

    temp = {'temp': round(random.uniform(15, 30), 2)}
    print(temp) 
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.temperature',
        body=json.dumps(temp)
    )
    sleep(1)
    
    # Dados de oxigênio
    oxygen = {'oxygen':  round(random.uniform(70, 90), 2)}
    print(oxygen)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.oxygen',
        body=json.dumps(oxygen)
    )
    sleep(1)

    # Dados de GPS
    gps = { 'lat': '{:.7f}'.format(random.randint(-90, 90) + random.random()/100),'lon': '{:.7f}'.format(random.randint(-180, 180) +random.random()/100) }
    print(gps)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.gps',
        body=json.dumps(gps)
    )
    sleep(2)
    
    # Dados de pressão
    pressure = { 'pressure': round(random.uniform(70, 90), 2) }
    print(pressure)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.pressure',
        body=json.dumps(pressure)
    )
    sleep(1.5)

connection.close()
