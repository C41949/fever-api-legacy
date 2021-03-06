import subprocess
from datetime import datetime

from commons import to_response as r
from database import db
from temperature.dtos import TemperatureListResponse
from temperature.models import Temperature


class TemperatureService:

    def __init__(self):
        self._command = "vcgencmd measure_temp | egrep -o '[0-9]*\\.[0-9]*'"

    def list(self) -> TemperatureListResponse:
        return Temperature.query.all()

    def create(self) -> Temperature:
        temperature = self.current_temperature()
        db.session.add(temperature)
        db.session.commit()
        return temperature

    def current_temperature(self) -> Temperature:
        return Temperature(temperature=self._current_temperature(), date=datetime.now())

    def _current_temperature(self) -> float:
        return float(subprocess.getoutput(self._command))
