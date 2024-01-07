from typing import Optional

import RPi.GPIO as GPIO
from config import settings


class PinReader:
    previous_state: Optional[int] = None
    current_state: Optional[int] = None
    time_state_changed: Optional[datetime] = None

    def __init__(self) -> None:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(settings.PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.update_state()

    def update_state(self) -> None:
        self.previous_state = self.current_state
        self.current_state = GPIO.input(settings.PIN)

    @property
    def state_changed(self):
        if self.previous_state is None and self.current_state == settings.DOOR_STATE.index("Door is open"):
            return True
        return self.previous_state != self.current_state

    @property
    def state_message(self):
        return f"[{settings.DOOR_NAME}] {settings.DOOR_STATE[self.current_state]}"
