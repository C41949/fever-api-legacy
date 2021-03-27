from sqlalchemy import Column, Integer, Float, DateTime

from database import db


class Temperature(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Float, nullable=False)
    date = Column(DateTime)
