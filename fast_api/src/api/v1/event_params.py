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
    key: str
    value: str

    @validator('key')
    def key_must_contain_userid_movieid(cls, value):
        if ':' not in value:
            raise ValueError('must contain ":"')
        try:
            user_id, movie_id = value.split(':')
            if not isinstance(uuid.UUID(user_id), UUID):
                raise ValueError('user_id  must be UUID')
            if not isinstance(uuid.UUID(movie_id), UUID):
                raise ValueError('movie_id must be UUID')
        except:
            raise ValueError(f'user_id and movie_id must be UUID. Key = {value}')
        return value


def get_event_params():
    return EventParams
