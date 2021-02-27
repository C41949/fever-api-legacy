from datetime import datetime
from typing import TypedDict


class TemperatureResponse(TypedDict):
    temperature: float
    date: datetime


class TemperatureListResponse(TypedDict):
    data: list[TemperatureResponse]
