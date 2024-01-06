from config import settings


class PushedRequest:
    app_key = settings.PUSHED_APP_KEY
    app_secret = settings.PUSHED_SECRET
    target_type = "channel"
    target_alias = "jMlKqi"

    def __init__(self, content=""):
        self.content = content
