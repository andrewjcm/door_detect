from config import settings


class PushedRequest:
    def __init__(self, content=""):
        self.content = content
        self.app_key = settings.PUSHED_APP_KEY
        self.app_secret = settings.PUSHED_SECRET
        self.target_type = "channel"
        self.target_alias = "jMlKqi"
