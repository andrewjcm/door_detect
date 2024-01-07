from services.api_request import BaseApiRequest
from services.pushed_co.schema import PushedRequest
from config import settings


class PushedApiRequest(BaseApiRequest):
    url = settings.PUSHED_API_URL
    status_code = None
    response = None

    def __init__(self, message):
        self.payload = PushedRequest(content=message).__dict__
