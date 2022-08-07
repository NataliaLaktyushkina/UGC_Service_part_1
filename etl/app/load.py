from clickhouse_driver import Client
from core.config import settings


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
                   '(user_id UUID, '
                   'movie_id UUID, '
                   'movie_timestamp DateTime ,'
                   'created_at DateTime) '
                   'Engine=MergeTree() ORDER BY id')


def load_data(data: dict, client: Client):
    if data:
        client.execute('INSERT INTO analytics.movie_view_history'
                       '(user_id, movie_id, movie_timestamp, created_at) '
                       'VALUES (%(user_id)s,'
                       '%(movie_id)s, %(movie_timestamp)s, %(created_at)s)s')
        # add logger 
        client.execute('SELECT * FROM analytics.movie_view_history')


def load(data: dict):
    client = create_client()
    create_db(client)
    create_table(client)
    load_data(data, client)


if __name__ == '__main__':
    data = {}
    load(data)
