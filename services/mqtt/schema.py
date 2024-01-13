from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class DoorState(Enum):
    OPEN = "open"
    CLOSED = "closed"


class MqttPayload(BaseModel):
    state: DoorState
    last_updated: datetime = datetime.now()
    last_changed: datetime
    name: Optional[str] = None
