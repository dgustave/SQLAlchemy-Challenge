# project/models/__init__.py

# Define tables and columns
 # Define tables and columns
from apps import Base, db
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship

    
def init_app(apps):
    db.init_app(apps)