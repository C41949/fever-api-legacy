from flask.blueprints import Blueprint

from temperature import TemperatureResponse, TemperatureListResponse, TemperatureService

temperatures = Blueprint(
    'temperatures',
    __name__
)

service = TemperatureService()


@temperatures.route('/temperature/current', methods=['GET'])
def current_temperature() -> TemperatureResponse:
    return service.current_temperature().to_response()


@temperatures.route('/temperature', methods=['GET'])
def list_temperatures() -> TemperatureListResponse:
    return service.list()
