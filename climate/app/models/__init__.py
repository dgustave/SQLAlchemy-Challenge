# project/models/__init__.py
# Define tables and columns
from .base import db

def init_app(app):
    db.init_app(app)