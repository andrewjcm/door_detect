from services.pin_reader import PinReader
import time


def main():
    pin_reader = PinReader()
    count = 0  # remove
    while count < 1000:
        time.sleep(.2)
        pin_reader.update_state()
        if pin_reader.state_changed:
            print(pin_reader.state_message)
        count += 1


if __name__ == "__main__":
    main()
