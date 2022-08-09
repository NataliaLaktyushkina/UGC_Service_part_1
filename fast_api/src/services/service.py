import abc

from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError

from models.events import EventMovieView


class AbstractEventStorage(abc.ABC):

    @abc.abstractmethod
    def send_event(self, event: EventMovieView, user_id: str) -> bool:
        pass


class KafkaEventStorage(AbstractEventStorage):
    def __init__(self, producer: AIOKafkaProducer):
        # producer does is enqueue the message on an internal queue which is later
        # (>= queue.buffering.max.ms) served by internal threads and sent to the broker
        self.producer = producer

    async def send_event(self, event: EventMovieView, user_id: str) -> bool:
        """Publishes records to the Kafka cluster"""

        # Get cluster layout and initial topic/partition leadership information
        await self.producer.start()

        try:
            # Produce message
            await self.producer.send_and_wait(topic=event.topic,
                                              value=event.value.encode(),
                                              key=':'.join((user_id, event.movie_id)).encode())

            event_was_sent = True
        except KafkaError as error:
            event_was_sent = False
        finally:
            # Wait for all pending messages to be delivered or expire.
            # Adding flush() before exiting will make the client wait for any outstanding messages
            # to be delivered to the broker
            await self.producer.flush()
        return event_was_sent
