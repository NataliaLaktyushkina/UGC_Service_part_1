from pydantic import Field

from .json_config import BaseOrjsonModel

from core.config import settings


class Event(BaseOrjsonModel):
    """
      This is the description of event model .
    """
    type: str = Field(..., description='type of event')


class EventMovieView(Event):
    topic = settings.TOPIC
    value: str
    key: str


class EventAccepted(BaseOrjsonModel):
    """
        This is the description of event response  model (event accepted or not)
    """
    accepted: bool
