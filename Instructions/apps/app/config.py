import os 

basedir = os.path.abspath.dirname(_file_))
# 1. Define base flask configuration. 
class Config: 
    """Base config, uses staging database server."""
    SECRET KEY = 'development key'
    ADMINS = frozenset([donley@gt.com, ]) #? if I run I will not be able to change

class DevelopmentConfig(Config): # 2. Development Configuration
    DEBUG = True
    SQLAlCHEMY_DATABASE_URI = "sqlite:///Resources/hawaii.sqlite"

class ProductionConfig(Config): # 3. Production Configuration
    SECRET KEY = 'Prod key'
    SQLAlCHEMY_DATABASE_URI = "sqlite:///Resources/hawaii.sqlite"

class TestingConfig(Config):
    TESTING = True

 # Note : 
    # Multiple processes can have the same database open at the same time. 
    # Multiple processes can be doing a SELECT at the same time. 
    # But only one process can be making changes to the database at any moment in time, however.
    # Addresses would be diffent if I pointed to an actual database, this a file

# 4. Dictionary maps name to configuration
Config = {
    'development': DevelopmentConfig, 
    'production': ProductionConfig, 
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
