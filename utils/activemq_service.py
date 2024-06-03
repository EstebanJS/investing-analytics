import os
import time
import stomp
from stomp.exception import ConnectFailedException

class ActiveMQService:
    def __init__(self):
        self.conn = stomp.Connection([(os.getenv("ACTIVEMQ_HOST", "localhost"), int(os.getenv("ACTIVEMQ_PORT", 61616)))])
        self.conn.set_listener('', self)
        self.subscribed_queues = {}
        self._connect()

    def _connect(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                self.conn.connect(os.getenv("ACTIVEMQ_USER", "admin"), os.getenv("ACTIVEMQ_PASSWORD", "admin"), wait=True)
                print("Connected to ActiveMQ")
                break
            except ConnectFailedException:
                print(f"Connection attempt {attempt + 1} failed. Retrying in 5 seconds...")
                time.sleep(5)
        else:
            print("Failed to connect to ActiveMQ after several attempts.")
            raise ConnectFailedException()

    def on_message(self, message):
        destination = message.headers.get('destination')
        if destination in self.subscribed_queues:
            self.subscribed_queues[destination](message)
        else:
            print(f'Received message from unknown destination: {message}')
            
    def on_error(self, message):
        print(f'received an error: {message}')

    def send_message(self, destination, message, headers):
        self.conn.send(headers=headers,body=message, destination=destination, persistent=True)

    def subscribe(self, destination, callback):
        self.conn.subscribe(destination=destination, id=destination, ack='auto')
        self.subscribed_queues[destination] = callback

    def disconnect(self):
        self.conn.disconnect()
