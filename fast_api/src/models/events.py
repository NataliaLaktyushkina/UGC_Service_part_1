from pydantic import Field, validator

from .json_config import BaseOrjsonModel

from core.config import settings
from datetime import datetime


class Event(BaseOrjsonModel):
    """
      This is the description of event model .
    """
    type: str = Field(..., description='type of event')


class EventMovieView(Event):
    topic = settings.TOPIC
    key: str
    value: str

    @validator('key')
    def key_must_contain_userid_movieid(cls, value):
        if ':' not in value:
            return ValueError('must contain :')
        return value

    @validator('value')
    def value_must_be_timestamp(cls, value):
        try:
            value_date = datetime.fromtimestamp(value)
        except OverflowError:
            return ValueError('must be timestamp')
        return value



class EventAccepted(BaseOrjsonModel):
    """
        This is the description of event response  model (event accepted or not)
    """
    accepted: bool


class  EventValidationError(BaseOrjsonModel):
    """
        pydantic validation error
    """
    text: str
