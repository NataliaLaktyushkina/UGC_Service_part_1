import abc
from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError


class AbstractEventStorage(abc.ABC):

    @abc.abstractmethod
    def send_event(self, event: str) -> bool:
        pass


class KafkaEventStorage(AbstractEventStorage):
    async def send_event(self, event: str) -> bool:
        producer = AIOKafkaProducer(bootstrap_servers='localhost:9092')
        # Get cluster layout and initial topic/partition leadership information
        await producer.start()
        try:
            # Produce message
            await producer.send_and_wait("my_topic", b"Super message")
            event_was_sent = True
        except KafkaError:
            event_was_sent = False
        finally:
            # Wait for all pending messages to be delivered or expire.
            await producer.stop()
        return event_was_sent
