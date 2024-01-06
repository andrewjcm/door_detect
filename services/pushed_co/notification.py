import requests
from services.pushed_co.schema import PushedRequest
from config import settings


class PushedApiRequest:
    url = settings.PUSHED_API_URL
    status_code = None
    response = None

    def send_notification(self, message):
        payload = PushedRequest(content=message)
        self.response = requests.post(self.url, data=payload)
        self.status_code = self.response.status_code

    @property
    def success(self):
        return self.status_code == 200
