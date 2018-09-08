import os

class Config:
    '''
    Configuration of our app features
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kwesi:OnnenOfori14@localhost/pitch'



class ProdConfig(Config):
    '''
    Class that sets app to run of production mode
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kwesi:OnnenOfori14@localhost/pitch'

class DevConfig(Config):
    """
    Class this sets app to run on development mode
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kwesi:OnnenOfori14@localhost/pitch'
    DEBUG = True

class TestConfig(Config):
    '''
    Class that sets app to run on test mode
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kwesi:OnnenOfori14@localhost/pitch'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
