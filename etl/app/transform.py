from load import load


def transform_data(kafka_data: dict):
    data = {}
    user_id, movie_id = data['key'].split(':')
    data['user_id'] = user_id
    data['movie_id'] = movie_id
    data['movie_timestamp'] = kafka_data['value']
    data['created_at'] = kafka_data['timestamp']

    load(data)