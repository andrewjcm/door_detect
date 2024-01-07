from services.api_request import BaseApiRequest
from services.pushover.schema import PushoverRequest
from config import settings


class PushoverApiRequest(BaseApiRequest):
    url = settings.PUSHOVER_URL

    def __init__(self, message):
        self.payload = PushoverRequest(message=message).__dict__
