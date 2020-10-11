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
    print({
                                'temp': round(random.uniform(20.1, 21.3), 2),
                              })
    channel.basic_publish(exchange='amq.topic',
                          routing_key='sensor.temperature',
                          body=json.dumps(
                              {
                                'temp': round(random.uniform(20.1, 21.3), 2),
                              }
                          ))
    sleep(.1)
    print({
                                'oxygen': '89',
                            })
    channel.basic_publish(exchange='amq.topic',
                        routing_key='sensor.oxygen',
                        body=json.dumps(
                            {
                                'oxygen': '89',
                            }
                        ))
    sleep(.3)
    print({
                                'lat': '-20.0000',
                                'lon': '-20.0000'
                            })
    channel.basic_publish(exchange='amq.topic',
                        routing_key='sensor.gps',
                        body=json.dumps(
                            {
                                'lat': '-20.0000',
                                'lon': '-20.0000'
                            }
                        ))
    sleep(.4)

connection.close()
