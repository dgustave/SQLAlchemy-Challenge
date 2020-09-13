# project/__init__.py
# Initialize Global Dependencies:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from app.settings import Config
# Abstract data from orm as models:
import jinja2

def create_app(config = None):
    app = Flask(__name__)
        # load default configuration
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
    print(f'ENV is set to: {app.config["ENV"]}')
    from . import models, views
    models.init_app(app)
    views.init_app(app)
    db.init_app(app)
    return app

