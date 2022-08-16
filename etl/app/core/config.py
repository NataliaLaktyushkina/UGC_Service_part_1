import os
from pydantic import BaseSettings, BaseModel
from dotenv import load_dotenv

IS_DOCKER = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)

if not IS_DOCKER:
    load_dotenv()   # take environment variables from .env.


class KafkaPromSettings(BaseModel):
    KAFKA_HOST: str = os.getenv('KAFKA_HOST')
    KAFKA_PORT: str = os.getenv('KAFKA_PORT')


class KafkaDevSettings(BaseModel):
    KAFKA_HOST: str = os.getenv('KAFKA_HOST_DEBUG')
    KAFKA_PORT: str = os.getenv('KAFKA_PORT_DEBUG')


class ClickHousePromSettings(BaseModel):
    CLICK_HOUSE_HOST: str = os.getenv('CLICK_HOUSE_HOST')
    CLICK_HOUSE_PORT: str = os.getenv('CLICK_HOUSE_PORT')


class ClickHouseDevSettings(BaseModel):
    CLICK_HOUSE_HOST: str = os.getenv('CLICK_HOUSE_HOST_DEBUG')
    CLICK_HOUSE_PORT: str = os.getenv('CLICK_HOUSE_PORT')


class Settings(BaseSettings):

    TOPIC: str = os.getenv('TOPIC')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class PromSettings(Settings):
    kafka_settings: KafkaPromSettings = KafkaPromSettings()
    click_house_settings: ClickHousePromSettings = ClickHousePromSettings()


class DevSettings(Settings):
    kafka_settings: KafkaDevSettings = KafkaDevSettings()
    click_house_settings: ClickHouseDevSettings = ClickHouseDevSettings()


def get_settings():
    environment = os.getenv('ENVIRONMENT')
    if environment == 'prom':
        return PromSettings()
    else:
        return DevSettings()


settings = get_settings()
