from infrastructure.message_broker.base.destination import MessageDestination


class RabbitMQDEventDestination(MessageDestination):
    routing_key: str
    exchange: str
