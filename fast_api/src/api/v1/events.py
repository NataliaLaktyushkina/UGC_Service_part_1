from fastapi import APIRouter, Depends, Query

from models.events import EventMovieView, EventAccepted, EventValidationError
from services.events import EventHandler, get_event_handler
from api.v1.event_params  import get_event_params
from services.jwt_check import JWTBearer

router = APIRouter()


@router.post('/', description="Post UGC event",
             response_model=EventAccepted,
             response_description='UGC event was posted')
async def post_event(event: EventMovieView = Depends(get_event_params()),
                     user_id: str= Depends(JWTBearer()),
                     service: EventHandler = Depends(get_event_handler)) -> EventAccepted:

    return await service.handle(event, user_id)
