from pydantic import AnyUrl

from services.api_request import BaseApiRequest
from services.pushed_co.schema import PushedRequest
from config import settings


class PushedApiRequest(BaseApiRequest):
    url: AnyUrl = settings.PUSHED_API_URL

    def __init__(self, message):
        self.payload = PushedRequest(content=message).__dict__
