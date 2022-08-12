from fastapi import APIRouter, Depends

from api.v1.event_params import EventParams
from models.events import EventMovieView, EventAccepted
from services.events import EventHandler, get_event_handler
from services.jwt_check import JWTBearer

router = APIRouter()


@router.post('/', description="Post UGC event",
             response_model=EventAccepted,
             response_description='UGC event was posted')
async def post_event(event: EventMovieView = Depends(EventParams),
                     user_id: str= Depends(JWTBearer()),
                     service: EventHandler = Depends(get_event_handler)) -> EventAccepted:

    return await service.handle(event, user_id)
