from load import load
import uuid
from datetime import datetime


async def transform_data(kafka_data: dict):
    data = {}
    user_id, movie_id = kafka_data['key'].decode('utf-8').split(':')
    data['user_id'] = uuid.UUID(user_id)
    data['movie_id'] = uuid.UUID(movie_id)
    movie_timestamp = kafka_data['value'].decode('utf-8')
    data['movie_timestamp'] = datetime.fromtimestamp(int(movie_timestamp))
    created_at = int(kafka_data['timestamp']/1000)
    data['created_at'] = datetime.fromtimestamp(created_at)

    await load(data)