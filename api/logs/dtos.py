from datetime import datetime
from typing import TypedDict

from logs.models import LogType


class LogResponse(TypedDict):
    id: int
    date: datetime
    type: LogType
    type: str


class LogListResponse(TypedDict):
    data: list[LogResponse]
