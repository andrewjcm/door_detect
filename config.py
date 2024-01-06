import os
import logging
from typing import List, Optional

from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class DoorState:
    OPEN = "Door is open"
    CLOSED = "Door is closed"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    DOOR_NAME: str = ""
    PIN: int = 3
    DOOR_STATE: List[str] = [DoorState.CLOSED, DoorState.OPEN]

    # pushed.co settings
    PUSHED_APP_KEY: Optional[str]
    PUSHED_SECRET: Optional[str]
    PUSHED_API_URL: Optional[AnyUrl]
    PUSHED_TARGET_TYPE: Optional[str]
    PUSHED_TARGET_ALIAS: Optional[str]

    # pushover settings
    PUSHOVER_TOKEN: Optional[str]
    PUSHOVER_USER: Optional[str]
    PUSHOVER_URL: Optional[AnyUrl]


settings = Settings()

