import uvicorn
from aiokafka import AIOKafkaProducer
from fastapi import FastAPI, Depends
from fastapi.responses import ORJSONResponse

from api.v1 import events
from core.config import settings
from db import eventbus_kafka
from services.jwt_check import JWTBearer

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

PROTECTED = [Depends(JWTBearer())]


@app.on_event('startup')
async def startup():
    kafka_settings = settings.kafka_settings
    eventbus_kafka.db_kafka = AIOKafkaProducer(
        bootstrap_servers=f'{kafka_settings.KAFKA_HOST}:{kafka_settings.KAFKA_PORT}',
        max_batch_size=1000)


@app.on_event('shutdown')
async def shutdown():
    await eventbus_kafka.db_kafka.stop()


app.include_router(events.router, prefix='/api/v1/events', tags=['events'], dependencies=PROTECTED)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8101,
    )
