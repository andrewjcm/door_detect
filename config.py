from typing import Optional

import logging
from systemd.journal import JournaldLogHandler

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

logger = logging.getLogger(__name__)
journald_handler = JournaldLogHandler()
journald_handler.setFormatter(logging.Formatter('[%(levelname)s]     %(message)s'))
logger.addHandler(journald_handler)
logger.setLevel(logging.INFO)
