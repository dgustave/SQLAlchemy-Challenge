 # Define tables and columns
 from app import db

class Measurements(db.model):
    __tablename__ = 'measurement'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    station = db.Column(db.String(30), nullable = False)
    date = db.Column(db.String(30), nullable = False)
    prcp = db.Column(db.FLOAT(), nullable = False)
    tobs = db.Column(db.FLOAT(), nullable = False)
    
class Stations(db.model):
    __tablename__ = 'station'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    station = db.Column(db.String(30), nullable = False)
    name = db.Column(db.String(30), nullable = False)
    latitude = db.Column(db.FLOAT(), nullable = False)
    longitude = db.Column(db.FLOAT(), nullable = False)
    elevation = db.Column(db.FLOAT(), nullable = False)
    