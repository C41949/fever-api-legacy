from sqlalchemy import Column, Integer, Float, DateTime

from database import db
from temperature import TemperatureResponse


class Temperature(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Float, nullable=False)
    date = Column(DateTime)

    def to_response(self) -> TemperatureResponse:
        return {'temperature': self.temperature, 'date': self.date}
