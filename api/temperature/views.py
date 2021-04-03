from flask import request
from flask.blueprints import Blueprint

from commons import to_response as r
from temperature.dtos import TemperatureResponse, TemperatureListResponse
from temperature.services import TemperatureService

temperatures = Blueprint('temperatures', __name__)

service = TemperatureService()


@temperatures.route('/temperature/current', methods=['GET'])
def current_temperature() -> TemperatureResponse:
    return r(service.current_temperature())


@temperatures.route('/temperature', methods=['POST'])
def create() -> TemperatureResponse:
    return r(service.create())


@temperatures.route('/temperature', methods=['GET'])
def list_temperatures() -> TemperatureListResponse:
    return {'data': [r(t) for t in service.list(service.build_filter(request))]}
