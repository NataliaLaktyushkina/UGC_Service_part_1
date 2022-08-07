import os
from pydantic import BaseSettings
from dotenv import load_dotenv

IS_DOCKER = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)

if not IS_DOCKER:
    load_dotenv()   # take environment variables from .env.


class Settings(BaseSettings):

    TOPIC: str = os.getenv('TOPIC')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class PromSettings(Settings):
    KAFKA_HOST: str = os.getenv('KAFKA_HOST')
    KAFKA_PORT: str = os.getenv('KAFKA_PORT')

    CLICK_HOUSE_HOST: str = os.getenv('CLICK_HOUSE_HOST')
    CLICK_HOUSE_PORT: str = os.getenv('CLICK_HOUSE_PORT')


class DevSettings(Settings):
    KAFKA_HOST: str
    KAFKA_PORT: str
    CLICK_HOUSE_HOST: str
    CLICK_HOUSE_PORT: str

    class Config:
        fields = {
            "KAFKA_HOST": {
                'env': 'KAFKA_HOST_DEBUG'
            },
            "KAFKA_PORT": {
                'env': 'KAFKA_PORT_DEBUG'
            },
            "CLICK_HOUSE_HOST": {
                'env': 'CLICK_HOUSE_HOST_DEBUG'
            },
            "CLICK_HOUSE_PORT": {
                'env': 'CLICK_HOUSE_PORT_DEBUG'
            }
        }


def get_settings():
    environment = os.getenv('ENVIRONMENT')
    if environment == 'prom':
        return get_prom_settings()
    else:
        return get_dev_settings()


def get_prom_settings():
    return PromSettings()


def get_dev_settings():
    return DevSettings()


settings = get_settings()
