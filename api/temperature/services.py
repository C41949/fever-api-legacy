import subprocess
from datetime import datetime, timedelta
from werkzeug.datastructures import MultiDict
from werkzeug.wrappers import BaseRequest

from database import db
from temperature.dtos import TemperatureResponse, ListFilter
from temperature.models import Temperature


class TemperatureService:

    def __init__(self):
        self._command = 'cat /sys/class/thermal/thermal_zone0/temp'

    def list(self, list_filter: ListFilter) -> list[TemperatureResponse]:
        return Temperature.query.filter(Temperature.date.between(list_filter['start'], list_filter['end'])).all()

    def create(self) -> Temperature:
        temperature = self.current_temperature()
        db.session.add(temperature)
        db.session.commit()
        return temperature

    def current_temperature(self) -> Temperature:
        return Temperature(temperature=self._current_temperature(), date=datetime.now())

    def _current_temperature(self) -> float:
        return float(subprocess.getoutput(self._command)) / 1000

    def build_filter(self, req: BaseRequest) -> ListFilter:
        query_params: MultiDict = req.args
        list_filter = {param: query_params.get(param) for param in ['start', 'end']}

        if not list_filter['start'] or not list_filter['end']:
            now = datetime.now()
            list_filter['start'] = str(now - timedelta(minutes=5))
            list_filter['end'] = str(now)

        return list_filter
