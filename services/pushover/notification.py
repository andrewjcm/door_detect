import requests
from services.pushover.schema import PushoverRequest
from config import settings


class PushoverApiRequest:
    url = settings.PUSHOVER_URL
    status_code = None
    response = None

    def send_notification(self, message):
        payload = PushoverRequest(message=message)
        self.response = requests.post(self.url, data=payload.__dict__)
        self.status_code = self.response.status_code

    @property
    def success(self):
        return self.status_code == requests.codes["ok"]
