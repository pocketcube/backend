#!/usr/bin/env python
import pika
import json
from time import sleep
import random
from datetime import datetime

credentials = pika.PlainCredentials('user', 'user')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()

while True:
    # Dados de temperatura
    temp = {'temperature': round(random.uniform(15, 30), 2), 'timestamp': str(datetime.now()) }
    print(temp) 
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.atmospheric',
        body=json.dumps(temp)
    )
    # Dados de pressão
    pressure = { 'pressure': round(random.uniform(70, 90), 2), 'timestamp': str(datetime.now()) }
    print(pressure)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.atmospheric',
        body=json.dumps(pressure)
    )
    # Dados de umidade
    humidity = { 'humidity': round(random.uniform(70, 90), 2), 'timestamp': str(datetime.now()) }
    print(humidity)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.atmospheric',
        body=json.dumps(humidity)
    )
    sleep(1.5)

    # Dados de latlong
    latlong = { 'lat': '{:.7f}'.format(random.randint(-90, 90) + random.random()/100),'lon': '{:.7f}'.format(random.randint(-180, 180) +random.random()/100), 'timestamp': str(datetime.now()) }
    print(latlong)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.gps',
        body=json.dumps(latlong)
    )

    # Dados de altitude
    altitude = { 'altitude': round(random.uniform(0, 150), 2), 'timestamp': str(datetime.now()) }
    print(altitude)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.gps',
        body=json.dumps(altitude)
    )

    # Dados de velocidade
    speed = { 'speed': round(random.uniform(0, 150), 2), 'timestamp': str(datetime.now()) }
    print(speed)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.gps',
        body=json.dumps(speed)
    )
    sleep(2)

    # Dados de no2
    no2 = { 'no2': round(random.uniform(70, 90), 2), 'timestamp': str(datetime.now()) }
    print(no2)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.gases',
        body=json.dumps(no2)
    )
    sleep(1.5)

    # Dados de nh3
    nh3 = { 'nh3': round(random.uniform(70, 90), 2), 'timestamp': str(datetime.now()) }
    print(nh3)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.gases',
        body=json.dumps(nh3)
    )
    sleep(1.5)

     # Dados de co2
    co2 = { 'co2': round(random.uniform(70, 90), 2), 'timestamp': str(datetime.now()) }
    print(co2)
    channel.basic_publish(
        exchange='amq.topic',
        routing_key='sensor.gases',
        body=json.dumps(co2)
    )
    sleep(1.5)

connection.close()
