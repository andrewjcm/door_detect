import requests
from config import settings


class NftyApiRequest:
    url = settings.NFTY_URL
    status_code = None
    response = None

    def send_notification(self, message):
        self.response = requests.post(self.url, data=message)
        self.status_code = self.response.status_code

    @property
    def success(self):
        return self.status_code == requests.codes["ok"]
