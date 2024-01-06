from config import settings
from pydantic import BaseModel


class PushedRequest(BaseModel):
    content: str = ""
    app_key: str = settings.PUSHED_APP_KEY
    app_secret: str = settings.PUSHED_SECRET
    target_type: str = settings.PUSHED_TARGET_TYPE
    target_alias: str = settings.PUSHED_TARGET_ALIAS
