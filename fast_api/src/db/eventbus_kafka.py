from typing import Optional

from aiokafka import AIOKafkaProducer

db_kafka: Optional[AIOKafkaProducer] = None


async def get_kafka() -> AIOKafkaProducer:
    return db_kafka
