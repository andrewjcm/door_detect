from typing import Optional
from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

import logging.config
import os


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    DOOR_NAME: str = ""
    PIN: int = 3

    # mqtt settings
    MQTT_USERNAME: Optional[str] = None
    MQTT_PASSWORD: Optional[str] = None
    MQTT_HOST: Optional[str] = None
    MQTT_TOPIC: Optional[str] = None

    # pushed.co settings
    PUSHED_APP_KEY: Optional[str] = None
    PUSHED_SECRET: Optional[str] = None
    PUSHED_API_URL: Optional[AnyUrl] = None
    PUSHED_TARGET_TYPE: Optional[str] = None
    PUSHED_TARGET_ALIAS: Optional[str] = None

    # pushover settings
    PUSHOVER_TOKEN: Optional[str] = None
    PUSHOVER_USER: Optional[str] = None
    PUSHOVER_URL: Optional[AnyUrl] = None

    # nfty settings
    NFTY_URL: Optional[AnyUrl] = None
    NFTY_TOPIC_ID: Optional[str] = None
    NFTY_TOKEN: Optional[str] = None


settings = Settings()

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default_formatter': {
            'format': '[%(levelname)s:%(asctime)s] %(message)s'
        },
    },
    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.path.abspath(os.getcwd()), "doordetect.log")
        }
    },
    'loggers': {
        'mainLogger': {
            'handlers': ['file', 'stream_handler'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('mainLogger')