### Procedure

1. The producer establishes a connection to a RabbitMQ instance
2. The producer creates exchanges and queues
3. The producer binds queues to exchanges
4. The producer publishes a message to an exchange
5. The exchange routes the message to one or more available queues. 
6. Sometimes it discards the message altogether
7. The consumer connects to one of the queues in the broker and consumes the available message
![alt text](image-1.png)

### Way of Starting Publisher and Consumer
They are separate services

We need to start them in different terminals