from typing import TypedDict
from flask import Flask
import subprocess

app = Flask(__name__)

TEMPERATURE_COMMAND = "vcgencmd measure_temp | egrep -o '[0-9]*\\.[0-9]*'"


class TemperatureResponse(TypedDict):
    temperature: float


@app.route('/temperature')
def get_temperature() -> TemperatureResponse:
    return {'temperature': _get_temperature()}


def _get_temperature() -> float:
    temperature = subprocess.getoutput(TEMPERATURE_COMMAND)
    return float(temperature)


if __name__ == '__main__':
    app.run()
