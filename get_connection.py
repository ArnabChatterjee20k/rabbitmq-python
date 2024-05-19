import pika

EXCHANGE = 'email_sending_exchange'
EXCHANGE_TYPE = 'direct'
QUEUE_NAME = "email_sending_queue"
ROUTING_KEY = "email_message"


def get_channel_connection():
    credentials = pika.PlainCredentials("user", "pass")
    # use urlparameters if used url from cloud
    params = pika.ConnectionParameters(host="localhost", credentials=credentials)
    connection = pika.BlockingConnection(params)

    # Producers and consumers talk to RabbitMQ via a channel.
    channel = connection.channel()

    # messages move from an exchange to a queue then bind them to queue
    
    # exchange created
    channel.exchange_declare(
        exchange=EXCHANGE,
        exchange_type=EXCHANGE_TYPE
    )

    # creating a queue
    channel.queue_declare(queue=QUEUE_NAME)

    # binding queue to exchange
    channel.queue_bind(
        QUEUE_NAME,
        EXCHANGE,
        ROUTING_KEY  # binding key
    )

    return channel,connection