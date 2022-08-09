import uuid
from uuid import UUID
from pydantic import Field, validator

from core.config import settings
from models.json_config import BaseOrjsonModel


class Event(BaseOrjsonModel):
    """
      This is the description of event model .
    """
    type: str = Field(..., description='type of event')


class EventParams(Event):
    topic = settings.TOPIC
    movie_id: str
    value: str

    @validator('movie_id')
    def movie_id_must_be_uuid(cls, value):
        if not isinstance(uuid.UUID(value), UUID):
            raise ValueError('movie_id must be UUID')
        return value


def get_event_params():
    return EventParams
