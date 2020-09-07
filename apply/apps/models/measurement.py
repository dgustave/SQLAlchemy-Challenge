from apply.apps.models import Column, Integer, String, ForeignKey, Date, Float

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