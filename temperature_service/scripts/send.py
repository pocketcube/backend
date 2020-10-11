#!/usr/bin/env python
import pika
import json
from time import sleep

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

while True:
    print('Sending')
    channel.basic_publish(exchange='amq.topic',
                          routing_key='sensor.temperature',
                          body=json.dumps(
                              {
                                  'lat': '-20.0000',
                                  'lon': '-20.0000'
                              }
                          ))
    sleep(.3)
connection.close()
