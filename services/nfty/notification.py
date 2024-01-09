import requests
from pydantic import AnyUrl

from config import settings
from services.api_request import BaseApiRequest


class NftyApiRequest(BaseApiRequest):
    url: AnyUrl = str(settings.NFTY_URL) + settings.NFTY_TOPIC_ID

    def __init__(self, message):
        self.payload = message

    def send(self):
        if not settings.NFTY_TOKEN:
            super().send()
        else:
            self.response = requests.post(
                self.url,
                data=self.payload,
                headers={"Authorization": f"Bearer {settings.NFTY_TOKEN}"}
            )
            self.status_code = self.response.status_code
