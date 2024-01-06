from services.pin_reader import PinReader
import time

from services.notification import send_pushed_notification


def main():
    pin_reader = PinReader()
    while True:
        time.sleep(.2)
        pin_reader.update_state()
        if pin_reader.state_changed:
            send_pushed_notification(pin_reader.state_message)


if __name__ == "__main__":
    main()
