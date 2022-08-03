import os
from pydantic import BaseSettings
from dotenv import load_dotenv

IS_DOCKER = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)

if not IS_DOCKER:
    load_dotenv()   # take environment variables from .env.


class Settings(BaseSettings):
    KAFKA_PORT: str = os.getenv('KAFKA_PORT')
    TOPIC: str = os.getenv('TOPIC')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class PromSettings(Settings):
    KAFKA_HOST: str = os.getenv('KAFKA_HOST')


class DevSettings(Settings):
    KAFKA_HOST: str

    class Config:
        fields = {
            "KAFKA_HOST": {
                'env': 'KAFKA_HOST_DEBUG'
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
