from services.pushed_co.notification import PushedApiRequest
from services.pushover.notification import PushoverApiRequest
from services.nfty.notification import NftyApiRequest
from config import settings, logger


def send_notification(message):
    if settings.PUSHED_API_URL:
        notification = PushedApiRequest(message)
        notification.send()
    elif settings.PUSHOVER_URL:
        notification = PushoverApiRequest(message)
        notification.send()
    elif settings.NFTY_URL:
        notification = NftyApiRequest(message)
        notification.send()
    else:
        notification = logger
        notification.info(msg=message)
    if hasattr(notification, "status_code"):
        log = logger
        if notification.success:
            log.info(msg=f"Message send successfully: {message}")
        else:
            log.error(msg=f"Error sending message: {notification.response.text}")
