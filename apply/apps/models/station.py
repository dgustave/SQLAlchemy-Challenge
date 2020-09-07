from apply.apps.models import Column, Integer, String, ForeignKey, Date, Float

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