from clickhouse_driver import Client
from core.config import settings


def create_client():
    client = Client(host=settings.CLICK_HOUSE_HOST)
    return client


def create_db(client: Client):
    client.execute('CREATE DATABASE '
                   'IF NOT EXISTS example '
                   'ON CLUSTER company_cluster')


def create_table(client: Client):
    client.execute('CREATE TABLE '
                   'IF NOT EXISTS example.regular_table ON CLUSTER company_cluster (id Int64, x Int32) '
                   'Engine=MergeTree() ORDER BY id')


def load_data(data: dict, client: Client):
    if data:
        client.execute('INSERT INTO example.regular_table (id, x) '
                       'VALUES (1, 10), (2, 20)')
        client.execute('SELECT * FROM example.regular_table')


def load(data: dict):
    client = create_client()
    create_db(client)
    create_table(client)
    load_data(data, client)


if __name__ == '__main__':
    data = {}
    load(data)
