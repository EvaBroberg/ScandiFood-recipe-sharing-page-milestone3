import os

#default config
class BaseConfig(object):
    DEBUG = False
    #mihht need to delete b
    SECRET_KEY = b"J/xb6R/x079/x8f/x02/xff/x84')/xaa X{/xf0"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

