from load import load
import uuid
from datetime import datetime
from typing import List


async def transform_data(kafka_data: List[dict]):
    processed_data = []
    for msg in kafka_data:
        data = {}
        user_id, movie_id = msg['key'].decode('utf-8').split(':')
        data['user_id'] = uuid.UUID(user_id)
        data['movie_id'] = uuid.UUID(movie_id)
        movie_timestamp = msg['value'].decode('utf-8')
        data['movie_timestamp'] = datetime.fromtimestamp(int(movie_timestamp))
        created_at = int(msg['timestamp']/1000)
        data['created_at'] = datetime.fromtimestamp(created_at)

        processed_data.append((
                uuid.uuid4(),
                data["user_id"],
                data["movie_id"],
                data["movie_timestamp"],
                data["created_at"],
            ))

    await load(processed_data)
