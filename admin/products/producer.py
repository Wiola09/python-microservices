import pika, json

import os

# Read RabbitMQ URL from environment variable
rabbitmq_url = os.getenv('RABBITMQ_URL', 'default_rabbitmq_url')

params = pika.URLParameters(rabbitmq_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
