from core.logger import logger
from transform import transform_data
from utils.etl_connection import connect_to_consumer


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
            if len(batch)>=2:
                await transform_data(kafka_data=batch)

    finally:
        await consumer.stop()

