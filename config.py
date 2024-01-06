from pydantic_settings import BaseSettings, SettingsConfigDict


class DoorState:
    OPEN = "Door is open"
    CLOSED = "Door is closed"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    PIN: int = 3
    PUSHED_APP_KEY: str
    PUSHED_SECRET: str
    PUSHED_API_URL: str


settings = Settings()
door_state = DoorState()
