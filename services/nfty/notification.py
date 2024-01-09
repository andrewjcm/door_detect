from pydantic import AnyUrl

from config import settings
from services.api_request import BaseApiRequest


class NftyApiRequest(BaseApiRequest):
    url: AnyUrl = str(settings.NFTY_URL) + settings.NFTY_TOPIC_ID

    def __init__(self, message):
        self.payload = message
        if settings.NFTY_TOKEN:
            self.url += f"?auth={settings.NFTY_TOKEN}"
