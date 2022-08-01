import abc
from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError


class AbstractEventStorage(abc.ABC):

    @abc.abstractmethod
    def send_event(self, event: str) -> bool:
        pass


class KafkaEventStorage(AbstractEventStorage):
    def __init__(self):
        self.producer = AIOKafkaProducer(bootstrap_servers='localhost:9092')

    async def send_event(self, event: str) -> bool:
        # Get cluster layout and initial topic/partition leadership information
        await self.producer.start()
        try:
            # Produce message
            await self.producer.send_and_wait("my_topic", b"Super message")
            event_was_sent = True
        except KafkaError:
            event_was_sent = False
        finally:
            # Wait for all pending messages to be delivered or expire.
            await self.producer.stop()
        return event_was_sent
