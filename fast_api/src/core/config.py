import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'UGC_API')

    KAFKA_PORT: str = os.getenv('KAFKA_PORT')

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