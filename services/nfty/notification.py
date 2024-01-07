from config import settings
from services.api_request import BaseApiRequest


class NftyApiRequest(BaseApiRequest):
    url = str(settings.NFTY_URL) + settings.NFTY_TOPIC_ID
    status_code = None
    response = None

    def __init__(self, message):
        self.payload = message
