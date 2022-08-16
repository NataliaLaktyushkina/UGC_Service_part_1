from pydantic import Field

from core.config import settings
from .json_config import BaseOrjsonModel


class Event(BaseOrjsonModel):
    """
      This is the description of event model .
    """
    type: str = Field(..., description='type of event')


class EventMovieView(Event):
    topic = settings.TOPIC
    movie_id: str
    value: str


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
