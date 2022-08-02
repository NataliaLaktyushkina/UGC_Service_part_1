from fastapi import APIRouter, Depends, Query

from models.events import EventMovieView, EventAccepted
from services.events import EventHandler, get_event_handler
from api.v1.event_params  import get_event_params

router = APIRouter()


@router.post('/', description="Post UGC event",
             response_model=EventAccepted,
             response_description='UGC event was posted')
async def post_event(event: EventMovieView = Depends(get_event_params()),
                     service: EventHandler = Depends(get_event_handler)) -> EventAccepted:
    return await service.handle(event)
