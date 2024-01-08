from services.board_headers.pin_reader import PinReader
import time

from services.notification import send_notification


def main():
    pin_reader = PinReader()
    while True:
        time.sleep(.2)
        pin_reader.update_state()
        if pin_reader.state_changed:
            send_notification(pin_reader.state_message)
        elif pin_reader.is_open_time_elapsed(incremental_minutes=30):
            send_notification(pin_reader.state_time_elapsed_message)


if __name__ == "__main__":
    main()
