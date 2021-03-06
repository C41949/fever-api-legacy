from commons import to_response as r
from database import db
from logs.dtos import LogListResponse
from logs.models import LogType, Log


class LogService:
    def create(self, log_type: LogType, message: str) -> Log:
        log = Log(type=log_type, message=message)
        db.session.add(log)
        db.session.commit()
        return log

    def list(self) -> LogListResponse:
        return Log.query.all()
