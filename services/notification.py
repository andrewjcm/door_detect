from services.pushed_co.notification import PushedApiRequest
from services.pushover.notification import PushoverApiRequest
from services.nfty.notification import NftyApiRequest
from config import settings
import logging

logger = logging.getLogger(__name__)


def send_notification(message):
    if settings.PUSHED_API_URL:
        notification = PushedApiRequest()
        notification.send_notification(message)
    elif settings.PUSHOVER_URL:
        notification = PushoverApiRequest()
        notification.send_notification(message)
    elif settings.NFTY_URL:
        notification = NftyApiRequest()
        notification.send_notification(message)
    else:
        notification = logger
        notification.info(msg=message)
    if hasattr(notification, "success"):
        log = logger
        if notification.success:
            log.info(msg=f"Message send successfully: {message}")
        else:
            log.error(msg=f"Error sending message: {notification.response.text}")
