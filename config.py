from typing import Optional

import logging.config

from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    DOOR_NAME: str = ""
    PIN: int = 3

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
    },
    'loggers': {
        'mainLogger': {
            'handlers': ['stream_handler'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('mainLogger')