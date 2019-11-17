from app import db
from models import Recipe

#create database and db tables
db.create_all()

#insert
db.session.add(Recipe("Something", "Make it like this"))
db.session.add(Recipe("Something else", "Make it like this and that"))

#commit the changes
db.session.commit()
