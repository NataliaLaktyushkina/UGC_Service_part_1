from typing import List

from aiochclient import ChClient
from aiohttp import ClientSession

from core.config import settings
from core.logger import logger


async def create_client(data: List[tuple]):
    async with ClientSession() as s:
        ch_settings = settings.click_house_settings
        client = ChClient(s, url=f'http://{ch_settings.CLICK_HOUSE_HOST}:{ch_settings.CLICK_HOUSE_PORT}')
        await create_db(client)
        await create_table(client)
        await load_data(data, client)


async def create_db(client: ChClient):
    await client.execute('CREATE DATABASE '
                         'IF NOT EXISTS analytics '
                         'ON CLUSTER company_cluster')


async def create_table(client: ChClient):
    await client.execute('CREATE TABLE '
                         'IF NOT EXISTS analytics.movie_view_history '
                         'ON CLUSTER company_cluster '
                         '(`id` UUID,'
                         '`user_id` UUID, '
                         '`movie_id` UUID, '
                         '`movie_timestamp` DateTime ,'
                         '`created_at` DateTime) '
                         'Engine=MergeTree() ORDER BY id')
    logger.info(await client.execute('SELECT * FROM analytics.movie_view_history'))


async def load_data(data: List[tuple], client: ChClient):
    if data:
        insert_query = 'INSERT INTO analytics.movie_view_history ' \
                       '(id, user_id, movie_id, movie_timestamp, created_at) ' \
                       ' VALUES '

        await client.execute(insert_query,
                             *data
                             )


async def load(data: List[tuple]):
    await create_client(data)
