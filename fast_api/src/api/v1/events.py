from fastapi import APIRouter, Depends
from models.events import Event, EventAccepted
from services.events import EventHandler, get_event_handler

router = APIRouter()


@router.post('/', description="Post UGC event",
             response_model=EventAccepted,
             response_description='UGC event was posted')
async def post_event(event: Event,
                     service: EventHandler = Depends(get_event_handler)) -> EventAccepted:
    return await service.handle(event)
