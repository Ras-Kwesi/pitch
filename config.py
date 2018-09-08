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
    pass

class DevConfig(Config):
    """
    Class this sets app to run on development mode
    """
    pass

class TestConfig(Config):
    '''
    Class that sets app to run on test mode
    '''
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
