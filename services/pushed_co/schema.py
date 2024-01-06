from config import settings


class PushedRequest:
    app_key = settings.PUSHED_APP_KEY
    app_secret = settings.PUSHED_SECRET
    target_type = "app"

    def __init__(self, content=""):
        self.content = content
