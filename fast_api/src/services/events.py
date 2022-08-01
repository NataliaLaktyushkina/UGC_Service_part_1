from fastapi import Depends
from service import AbstractEventStorage, KafkaEventStorage
from db.oltp_kafka import get_kafka
from models.events import EventMovieView, EventAccepted


class EventHandler:
    def __init__(self, event_storage: AbstractEventStorage):
        self.event_storage = event_storage

    async def handle(self, event: EventMovieView) -> EventAccepted:
        event_accepted = await self.event_storage.send_event(event)
        return event_accepted


def get_event_handler(
        event_storage: AbstractEventStorage = Depends(get_kafka)
) -> EventHandler:
    return EventHandler(KafkaEventStorage(event_storage))
