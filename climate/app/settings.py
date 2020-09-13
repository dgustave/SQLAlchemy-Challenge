import os 

BASE_DIR = os.path.abspath(os.path.dirname(__name__))
# 1. Define base flask configuration. 
class Config: 
    """Base config, uses staging database server."""
    SQLAlCHEMY_DATABASE_URI = "sqlite:///Resources/hawaii.sqlite"
    DEBUG = False

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

class DevelopmentConfig(Config): 
    DB_SERVER = 'localhost'
    DEBUG = True
    
class ProductionConfig(Config): 
    DEBUG = False

class TestingConfig(Config):
    TESTING = True


# Dictionary maps name to configuration
Config = {
    'development': DevelopmentConfig, 
    'production': ProductionConfig, 
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
