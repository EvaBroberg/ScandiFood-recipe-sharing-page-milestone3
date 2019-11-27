import os

#default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "super secret key"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

