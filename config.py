import os
import logging
from typing import List

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


class PushedCoSettings(Settings):
    PUSHED_APP_KEY: str
    PUSHED_SECRET: str
    PUSHED_API_URL: AnyUrl
    PUSHED_TARGET_TYPE: str
    PUSHED_TARGET_ALIAS: str


class PushoverSettings(Settings):
    PUSHOVER_TOKEN: str
    PUSHOVER_USER: str
    PUSHOVER_URL: AnyUrl


if os.getenv("PUSHED_API_URL"):
    settings = PushedCoSettings()
elif os.getenv("PUSHOVER_URL"):
    settings = PushoverSettings()
else:
    settings = Settings()

