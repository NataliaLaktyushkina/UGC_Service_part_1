from fastapi import Depends
from services.service import AbstractEventStorage, KafkaEventStorage
from db.eventbus_kafka import get_kafka
from models.events import EventMovieView, EventAccepted


class EventHandler:
    def __init__(self, event_storage: AbstractEventStorage):
        self.event_storage = event_storage

    async def handle(self, event: EventMovieView, user_id: str) -> EventAccepted:
        event_accepted = await self.event_storage.send_event(event, user_id)
        return EventAccepted(accepted=event_accepted)


def get_event_handler(
        event_storage: AbstractEventStorage = Depends(get_kafka)
) -> EventHandler:
    return EventHandler(KafkaEventStorage(event_storage))
