from app import jsonify, settings
from app.models import Measurement, Station, func, engine, db
from sqlalchemy.orm import Session 
from datetime import datetime as dt

session = Session(engine)

# find the last date in the database
last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

# Calculate the date 1 year ago from the last data point in the database
query_date = dt.date(2017,8,23) - dt.timedelta(days=365)

session.close()


# Home page.
# List all routes that are available.

@app.route('/')
def index():
    return  ("""List all available api routes."""
    f"Available Routes:<br/>"
    f"Precipitation: /api/v1.0/precipitation<br/>"
    f"Stations: /api/v1.0/stations<br/>"
    f"Temperature for a year: /api/v1.0/tobs<br/>"
    f"Temperature stat from the start date(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd<br/>"
    f"Temperature stat from start to end dates(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    f"Flask environment is set to: {settings['ENV']}")
  
    # render_template("index.html")
    
          
# Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
# Return the JSON representation of your dictionary.
@app.route('/api/v1.0/precipitation')
def precipitation():
    sel = [Measurement.date,Measurement.prcp]
    queryresult = session.query(*sel).all()
    session.close()

    precipitation = []
    for date, prcp in queryresult:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation.append(prcp_dict)

    return jsonify(precipitation)


#Return a JSON list of stations from the dataset.
@app.route('/api/v1.0/stations')
def stations():
    sel = [Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation]
    queryresult = session.query(*sel).all()
    session.close()
    stations = []
    for station,name,lat,lon,el in queryresult:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Lat"] = lat
        station_dict["Lon"] = lon
        station_dict["Elevation"] = el
        stations.append(station_dict)

    return jsonify(stations)

@app.route('/api/v1.0/tobs')
# Query the dates and temperature observations of the most active station for the last year of data.
  
# Return a JSON list of temperature observations (TOBS) for the previous year.
def tobs():
    lateststr = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latestdate = dt.datetime.strptime(lateststr, '%Y-%m-%d')
    querydate = dt.date(latestdate.year -1, latestdate.month, latestdate.day)
    sel = [Measurement.date,Measurement.tobs]
    queryresult = session.query(*sel).filter(Measurement.date >= querydate).all()
    session.close()

    tobsall = []
    for date, tobs in queryresult:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs
        tobsall.append(tobs_dict)

    return jsonify(tobsall)

# Return a JSON list of the minimum temperature, the average temperature, and the max #       temperature for a given start or start-end range:
           
# When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date: 
           
@app.route('/api/v1.0/<start>')
def get_start(start):
    queryresult = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    session.close()

    tobsall = []
    for min,avg,max in queryresult:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobsall.append(tobs_dict)

    return jsonify(tobsall)

# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive:
@app.route('/api/v1.0/<start>/<end>')
def get_start_end(start,end):
    queryresult = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()

    tobsall = []
    for min,avg,max in queryresult:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobsall.append(tobs_dict)
    return jsonify(tobsall)

def init_app(app):
    app.register_blueprint(Measurement)
    app.register_blueprint(Station)   
    db.init_app(app)
    
