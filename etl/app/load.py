from clickhouse_driver import Client
from core.config import settings
from core.logger import logger


def create_client():
    client = Client(host=settings.CLICK_HOUSE_HOST)
    return client


def create_db(client: Client):
    client.execute('CREATE DATABASE '
                   'IF NOT EXISTS analytics '
                   'ON CLUSTER company_cluster')


def create_table(client: Client):
    client.execute('CREATE TABLE '
                   'IF NOT EXISTS analytics.movie_view_history '
                   'ON CLUSTER company_cluster '
                   '(id UUID,'
                   'user_id UUID, '
                   'movie_id UUID, '
                   'movie_timestamp DateTime ,'
                   'created_at DateTime) '
                   'Engine=MergeTree() ORDER BY id')
    client.execute('SELECT * FROM analytics.movie_view_history')


def load_data(data: dict, client: Client):
    if data:
        insert_query = 'INSERT INTO analytics.movie_view_history ' \
                       '(id, user_id, movie_id, movie_timestamp, created_at) ' \
                       ' VALUES (generateUUIDv4(), %(user_id)s,' \
                       '%(movie_id)s, %(movie_timestamp)s, %(created_at)s)'

        client.execute(query=insert_query,
                       params=data)
        # check
        logger.info(client.execute('SELECT * FROM analytics.movie_view_history '
                                   'ORDER BY created_at desc '
                                   'LIMIT 1'))


def load(data: dict):
    client = create_client()
    create_db(client)
    create_table(client)
    load_data(data, client)


if __name__ == '__main__':
    data = {'user_id': '49d9bf90-780f-4a1b-862a-1291af77b624',
            'movie_id': '5ab0ad6c-d190-445e-a260-d79460e49394',
            'movie_timestamp': '1659508485',
            'created_at': '1659508485'}
    load(data)
