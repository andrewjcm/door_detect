from typing import Optional
from datetime import datetime, timedelta
import RPi.GPIO as GPIO

from services.board_headers.enums import DoorState
from config import settings


class PinReader:
    previous_state: Optional[DoorState] = None
    current_state: Optional[DoorState] = None
    time_state_changed: Optional[datetime] = None

    def __init__(self) -> None:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(settings.PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def update_state(self) -> None:
        self.previous_state = self.current_state
        self.current_state = DoorState(GPIO.input(settings.PIN))
        if self.state_changed:
            self.time_state_changed = datetime.now()

    @property
    def state_changed(self) -> bool:
        return self.previous_state != self.current_state

    @property
    def state_message(self) -> str:
        return f"[{settings.DOOR_NAME}] Door is {self.current_state.name}"

    @property
    def state_time_elapsed_message(self) -> str:
        return self.state_message + f" (time elapsed: {self.time_passed_since_state_change})"

    @property
    def time_passed_since_state_change(self) -> timedelta:
        return datetime.now() - self.time_state_changed

    @property
    def time_passed_since_state_change_minutes(self) -> int:
        return self.time_passed_since_state_change.seconds // 60

    @property
    def is_open(self) -> bool:
        return self.current_state == DoorState.OPEN

    def is_open_time_elapsed(self, incremental_minutes: int) -> bool:
        return (
                self.is_open
                and self.time_passed_since_state_change_minutes > 0
                and self.time_passed_since_state_change_minutes % incremental_minutes == 0
        )
