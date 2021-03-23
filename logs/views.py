from flask.blueprints import Blueprint

from commons import to_response as r
from logs.services import LogService

logs = Blueprint('logs', __name__)

service = LogService()


@logs.route('/log', methods=['GET'])
def list_logs():
    return {'data': [r(log) for log in service.list()]}

