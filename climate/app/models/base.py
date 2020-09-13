from flask import current_app
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func, Column, String, Integer, Date, Float
# reflect an existing database into a new model
Base = automap_base()

# Save references to each table
class Measurement(Base):
    __tablename__ = 'measurement'
    id = Column(Integer, primary_key=True, nullable=False)
    station = Column(String(30), nullable = False)
    date = Column(Date, nullable = False)
    prcp = Column(Float(), nullable = False)
    tobs = Column(Float(), nullable = False)
    def __repr__(self):
        return "Measurements(id = {self.id},"\
    "station = '{self.station}',"\
    "date = {self.date},"\
    "prcp = {self.prcp},"\
    "tobs = {self.tobs})".format(self=self)

class Station(Base):
    __tablename__ = 'station'
    id = Column(Integer, primary_key=True, nullable=False)
    station = Column(String(30), nullable = False)
    name = Column(String(30), nullable = False)
    latitude = Column(Float(), nullable = False)
    longitude = Column(Float(), nullable = False)
    elevation = Column(Float(), nullable = False)
    def __repr__(self):
        return "Measurements(id = {self.id},"\
    "station = '{self.station}',"\
    "name = '{self.name}',"\
    "latitude = {self.latitude},"\
    "longitude = {self.longitude},"\
    "elevation = {self.elevation})".format(self=self)

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

