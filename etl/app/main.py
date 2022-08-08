import asyncio

from extract import extract_data
from utils.etl_connection import backoff



async def etl():
    while True:
        data = await extract_data()


if __name__ == '__main__':
    asyncio.run(etl())
