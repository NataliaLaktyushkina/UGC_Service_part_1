from core.logger import logger
from transform import transform_data
from utils.etl_connection import connect_to_consumer


async def extract_data():
    consumer = connect_to_consumer()
    await consumer.start()
    try:
        async for msg in consumer:

            data = {'topic': msg.topic,
                    'key': msg.key,  # user_id:movie_id
                    'value': msg.value,
                    'timestamp': msg.timestamp}
            logger.info(msg=data)

            transform_data(kafka_data=data)

    finally:
        await consumer.stop()

