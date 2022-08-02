import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import events
from db import oltp_kafka
from aiokafka import AIOKafkaProducer
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    oltp_kafka.db_kafka = AIOKafkaProducer(bootstrap_servers=f'{settings.KAFKA_HOST}:{settings.KAFKA_PORT}')


@app.on_event('shutdown')
async def shutdown():
    await oltp_kafka.db_kafka.stop()


app.include_router(events.router, prefix='/api/v1/events', tags=['events'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8101,
    )
