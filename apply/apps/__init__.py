# project/__init__.py
import os
from flask import Flask
# Initialize Global Dependencies:
from flask import Flask, Model, apps
# Abstract data from orm as models:
from flask_sqlalchemy import SQLAlchemy, AppBuilder
import jinja2
db = SQLAlchemy()


def create_app(config = None):
    from . import models, views
    app = Flask(__name__)
    # load default configuration
    app.config.from_object('apps.settings')
    if app.config["ENV"] == 'production': 
        app.config.from_object("config[ProductionConfig]") 
    elif app.config["ENV"] == 'testing':
        app.config.from_object("config[TestingConfig]") 
    else: 
        app.config.from_object("config[DevelopmentConfig]") 
    models.init_app(app)
    views.init_app(app)
    return app