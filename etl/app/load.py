from clickhouse_driver import Client
from core.config import settings


def load_data():
    client = Client(host=settings.CLICK_HOUSE_HOST)

    client.execute('CREATE DATABASE IF NOT EXISTS example ON CLUSTER company_cluster')

    client.execute('CREATE TABLE example.regular_table ON CLUSTER company_cluster (id Int64, x Int32) '
                   'Engine=MergeTree() ORDER BY id')

    client.execute('INSERT INTO example.regular_table (id, x) VALUES (1, 10), (2, 20)')

    client.execute('SELECT * FROM example.regular_table')


load_data()