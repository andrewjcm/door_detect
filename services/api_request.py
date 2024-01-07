from typing import Union

import requests
from pydantic import AnyUrl


class BaseApiRequest:
    url: AnyUrl
    payload: Union[dict, str]
    status_code = None
    response = None

    def send_notification(self):
        self.response = requests.post(self.url, data=self.payload)
        self.status_code = self.response.status_code

    @property
    def success(self):
        return self.status_code == requests.codes["ok"]
