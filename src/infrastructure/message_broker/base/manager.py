from abc import ABC, abstractmethod

from infrastructure.message_broker.base.destination import MessageDestination


class MessageBrokerPublisher[DESTINATION: MessageDestination](ABC):

    @abstractmethod
    async def publish(self, message: bytes, destination: DESTINATION) -> None: ...
