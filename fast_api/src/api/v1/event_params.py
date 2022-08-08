
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
        return value


def get_event_params():
    return EventParams
