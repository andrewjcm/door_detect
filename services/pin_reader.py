from typing import Optional

import RPi.GPIO as GPIO
from config import settings
from datetime import datetime, timedelta


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
        if self.state_changed:
            self.time_state_changed = datetime.now()

    @property
    def state_changed(self) -> bool:
        if self.previous_state is None and self.is_open:
            return True
        return self.previous_state != self.current_state

    @property
    def state_message(self) -> str:
        return f"[{settings.DOOR_NAME}] {settings.DOOR_STATE[self.current_state]}"

    @property
    def state_time_elapsed_message(self) -> str:
        return self.state_message + f"(time elapsed: {self.time_passed_since_state_change})"

    @property
    def time_passed_since_state_change(self) -> timedelta:
        return datetime.now() - self.time_state_changed

    @property
    def time_passed_since_state_change_minutes(self) -> int:
        return self.time_passed_since_state_change.seconds // 3600

    @property
    def is_open(self) -> bool:
        return self.current_state == settings.DOOR_STATE.index("Door is open")

    def is_open_time_elapsed(self, incremental_minutes) -> bool:
        return (
                self.is_open
                and self.time_passed_since_state_change_minutes > 0
                and self.time_passed_since_state_change_minutes % incremental_minutes == 0
        )
