from __future__ import print_function

import pika
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body='Hello World!')
    connection.close()
    return "holo!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
