from pydantic import Field

from .json_config import BaseOrjsonModel


class Event(BaseOrjsonModel):
    """
      This is the description of event model .
    """
    type: str = Field(..., description='type of event')


class EventAccepted(BaseOrjsonModel):
    """
        This is the description of event response  model (event caught or not)
    """
    accepted: bool
