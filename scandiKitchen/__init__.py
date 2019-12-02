import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#setup database
basedir = os.path.abspath(os.path.dirname(__file__))
#set up connection to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK+MODIFICATIONS'] = False

#create database
db = SQLAlchemy(app)
#connect app to database
Migrate(app,db)

from scandiKitchen.core.views import core
app.register_blueprint(core)
