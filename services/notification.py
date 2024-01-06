from services.pushed_co.notification import PushedApiRequest


def send_pushed_notification(message):
    pushed = PushedApiRequest()
    pushed.send_notification(message)
    if not pushed.success:
        print("Error sending message")
