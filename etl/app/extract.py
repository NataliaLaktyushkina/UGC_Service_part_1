from core.logger import logger
from transform import transform_data
from utils.etl_connection import connect_to_consumer
from core.config import settings


async def extract_data():
    consumer = connect_to_consumer()
    await consumer.start()
    try:
        batch = []
        async for msg in consumer:


            data = {'topic': msg.topic,
                    'key': msg.key,  # user_id:movie_id
                    'value': msg.value,
                    'timestamp': msg.timestamp}
            logger.info(msg=data)
            batch.append(data)
            if len(batch) >= settings.BATCH_SIZE:
                await transform_data(kafka_data=batch)
                batch = []

    finally:
        await consumer.stop()

