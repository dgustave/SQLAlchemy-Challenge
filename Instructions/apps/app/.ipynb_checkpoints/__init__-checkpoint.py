# Initialize Global Dependencies:
import sqlalchemy 
from flask import Flask
from flask import SQLAlchemy 
from config import config 
from models import Measurements, Stations

# 1. Creates an unconfigured instance
db = SQLAlchemy()

# 2. Defines the create_app app factory: 
    # A common pattern is creating the application object when the blueprint is imported. 
    # If the creation of this object into a function, you can then create multiple instances of this app later.
def create_app(config_name): # 1.
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.Initialize(app) #3.
    return app 

# 3. Initialize the instance per app context. 

# Notes: 
    # When the app is run it will run the entire models module and then its dependencies. 
    # Restructure  models dependencies, because import will db reference from app name. Instead from __main__ import db.
    # This doesn't solve the problem because now imports can't import db from __main__
    # Watch out for circular routes