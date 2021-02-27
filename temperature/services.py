import subprocess
from datetime import datetime

from database import db
from temperature import Temperature, TemperatureListResponse


class TemperatureService:

    def __init__(self):
        self._command = "vcgencmd measure_temp | egrep -o '[0-9]*\\.[0-9]*'"

    def list(self) -> TemperatureListResponse:
        return {'data': [t.to_response() for t in Temperature.query.all()]}

    def create(self) -> Temperature:
        temperature = self.current_temperature()
        db.session.add(temperature)
        db.session.commit()
        return temperature

    def current_temperature(self) -> Temperature:
        return Temperature(temperature=self._current_temperature(), date=datetime.now())

    def _current_temperature(self) -> float:
        return float(subprocess.getoutput(self._command))
