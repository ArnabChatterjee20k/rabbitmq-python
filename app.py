from flask import Flask
from get_connection import get_channel_connection , EXCHANGE,ROUTING_KEY
app = Flask(__name__)

@app.get("/<name>")
def home(name):
    channel,connection = get_channel_connection()
    with connection:
        channel.basic_publish(
            exchange=EXCHANGE,
            routing_key=ROUTING_KEY,
            body=name
        )
    print(connection.is_open)
    return "saved",201

app.run(debug=True)