class Config(object):
    """
    Common configurations
    """
    SQLALCHEMY_DATABASE_URI = 'postgres://db_user:db_password@localhost/lesson'



class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}