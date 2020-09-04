 # Define tables and columns
 from app import db

class Measurements(db.model):
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    station = db.Column(db.String(30), nullable = False)
    date = db.Column(db.String(30), nullable = False)
    prcp = db.Column(db.FLOAT(), nullable = False)
    tobs = db.Column(db.FLOAT(), nullable = False)