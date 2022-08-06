from utils.etl_connection import connect_to_consumer
from core.logger import logger


async def extract_data():
    consumer = connect_to_consumer()
    await consumer.start()
    try:
        async for msg in consumer:

            data = {'topic': msg.topic,
                    'key': msg.key,
                    'value': msg.value,
                    'timestamp': msg.timestamp}
            logger.info(msg=data)

    finally:
        await consumer.stop()

