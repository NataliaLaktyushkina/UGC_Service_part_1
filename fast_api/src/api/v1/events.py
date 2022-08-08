from fastapi import APIRouter, Depends, Query

from models.events import EventMovieView, EventAccepted, EventValidationError
from services.events import EventHandler, get_event_handler
from api.v1.event_params  import get_event_params
from typing import Union

router = APIRouter()


@router.post('/', description="Post UGC event",
             response_model=Union[EventAccepted, EventValidationError],
             response_description='UGC event was posted')
async def post_event(event: EventMovieView = Depends(get_event_params()),
                     service: EventHandler = Depends(get_event_handler)) -> Union[EventAccepted, EventValidationError]:
    if not isinstance(event.key, str):
        return EventValidationError(text=event.key)
    return await service.handle(event)
