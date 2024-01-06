from config import settings
from pydantic import BaseModel


class PushoverRequest(BaseModel):
    message: str = ""
    token: str = settings.PUSHOVER_TOKEN
    user: str = settings.PUSHOVER_USER
