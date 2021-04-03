from datetime import datetime
from typing import TypedDict


class TemperatureResponse(TypedDict):
    id: int
    temperature: float
    date: datetime


class TemperatureListResponse(TypedDict):
    data: list[TemperatureResponse]


class ListFilter(TypedDict):
    start: str
    end: str
