from services.board_headers.pin_reader import PinReader
import time

from services.notification import send_notification


def main():
    pin_reader = PinReader()
    notification_sent_time_elapsed = 0
    while True:
        pin_reader.update_state()
        if pin_reader.state_changed:
            send_notification(pin_reader.state_message)
        elif (
                pin_reader.is_open_time_elapsed(incremental_minutes=30)
                and pin_reader.time_passed_since_state_change_minutes > notification_sent_time_elapsed
        ):
            send_notification(pin_reader.state_time_elapsed_message)
            notification_sent_time_elapsed = pin_reader.time_passed_since_state_change_minutes
        time.sleep(.2)


if __name__ == "__main__":
    main()
