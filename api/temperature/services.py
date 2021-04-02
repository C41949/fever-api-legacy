import subprocess
from datetime import datetime

from database import db
from temperature.dtos import TemperatureListResponse
from temperature.models import Temperature


class TemperatureService:

    def __init__(self):
        self._command = 'cat /sys/class/thermal/thermal_zone0/temp'

    def list(self) -> TemperatureListResponse:
        # TODO Temporary fix
        return Temperature.query.limit(300).all()

    def create(self) -> Temperature:
        temperature = self.current_temperature()
        db.session.add(temperature)
        db.session.commit()
        return temperature

    def current_temperature(self) -> Temperature:
        return Temperature(temperature=self._current_temperature(), date=datetime.now())

    def _current_temperature(self) -> float:
        return float(subprocess.getoutput(self._command)) / 1000
