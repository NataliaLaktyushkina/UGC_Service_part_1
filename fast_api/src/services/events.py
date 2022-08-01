from fastapi import Depends
from service import AbstractEventStorage, Kafka_Event_Storage
from aiokafka import AIOKafkaProducer


class EventHandler:
    def __init__(self, event_storage: AbstractEventStorage):
        self.event_storage = event_storage

    async def handle(self, event):
        event_accepted = await self.event_storage.send_event(event)
        return event_accepted


def get_event_handler(
        event_storage: AbstractEventStorage = Depends(get_kafka)
) -> EventHandler:
    return EventHandler(AIOKafkaProducer(event_storage))
