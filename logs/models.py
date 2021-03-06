import enum

from sqlalchemy import Column, Integer, DateTime, func, Enum, String

from database import db


class LogType(str, enum.Enum):
    MESSAGE = 'MESSAGE'
    ERROR = 'ERROR'
    WARNING = 'WARNING'


class Log(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, server_default=func.now())
    type = Column(Enum(LogType), nullable=False)
    message = Column(String, nullable=False)
