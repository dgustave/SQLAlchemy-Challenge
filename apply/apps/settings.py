import os 
from apply.config import DevelopmentConfig, ProductionConfig, TestingConfig
# 1. Define base flask configuration. 
class Config: 
    """Base config, uses staging database server."""
    SQLAlCHEMY_DATABASE_URI = "sqlite:///Resources/hawaii.sqlite"
    DEBUG = False

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


    # Dictionary maps name to configuration
Config = {
    'development': DevelopmentConfig, 
    'production': ProductionConfig, 
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
