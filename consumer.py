import pika,os,time
from get_connection import get_channel_connection, QUEUE_NAME,ROUTING_KEY


def save_email(msg):
    with open("names.txt",'a+') as f:
        f.write(msg)

# create a function which is called on incoming messages
def callback(ch, method, properties, body:bytes):
  print(body)
  save_email(str(body))

channel,connection = get_channel_connection()
channel.basic_consume(
 queue=QUEUE_NAME,
 on_message_callback=callback,
 auto_ack=True   
)

channel.start_consuming()
connection.close()