from services.pushed_co.notification import PushedApiRequest
from services.pushover.notification import PushoverApiRequest
from config import settings
import logging

logger = logging.getLogger(__name__)


def send_notification(message):
    if hasattr(settings, "PUSHED_API_URL"):
        notification = PushedApiRequest()
        notification.send_notification(message)
    elif hasattr(settings, "PUSHOVER_URL"):
        notification = PushoverApiRequest()
        notification.send_notification(message)
    else:
        notification = logger
        notification.info(msg=message)
    if hasattr(settings, "success"):
        log = logger
        if notification.success:
            log.info(msg=message)
        else:
            log.error(msg=f"Error sending message: {notification.response.text}")
