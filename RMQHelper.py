import os
import json
import pika
from typing import Callable
# from pika.exchange_type import ExchangeType


class RMQHelper:

    EXCHANGE = 'email_sending_exchange'
    EXCHANGE_TYPE = 'direct'
    QUEUE_NAME = "email_sending_queue"
    ROUTING_KEY = "email_message"

    def __init__(self) -> None:
        """ Sets up a connection and a channel when this class is instantiated """
        credentials = pika.PlainCredentials("user", "pass")
        params = pika.ConnectionParameters(host="localhost", credentials=credentials)

        self.__connection = pika.BlockingConnection(
            params)

    def __create_channel(self) -> pika.BlockingConnection:
        channel = self.__connection.channel()  # start a channel
        return channel

    async def __create_exchanges_queues(self) -> None:
        """ Declares a queue and an exchange using the channel created """
        # Get channel
        channel = self.__create_channel()
        # Create an exchange
        channel.exchange_declare(
            exchange=self.EXCHANGE, exchange_type=self.EXCHANGE_TYPE
        )
        # Create a queue
        channel.queue_declare(queue=self.QUEUE_NAME)
        # Bind queue with exchange
        channel.queue_bind(
            self.QUEUE_NAME,
            self.EXCHANGE,
            self.ROUTING_KEY  # The routing key here is the binding key
        )

    def publish_message(self, message_body) -> None:
        """ Publishes a message to RMQ """
        # First declare an exchange and a queue
        self.__create_exchanges_queues()

        # Get channel
        channel = self.__create_channel()

        channel.basic_publish(
            exchange=self.EXCHANGE,
            routing_key=self.ROUTING_KEY,
            body=json.dumps(message_body)
        )

        print("[x] Message sent to consumer")

        self.__connection.close()


    def consume_message(self, callback: Callable) -> None:
        """ Reads a message published to a queue it's bound to """
        self.__create_queue()
        # Get channel
        channel = self.__create_channel()
        channel.basic_consume(
            self.QUEUE_NAME,
            callback,
            auto_ack=True
        )
        # start consuming (blocks)
        channel.start_consuming()
        self.connection.close()


# Create an instance
rmq: RMQHelper = RMQHelper()
