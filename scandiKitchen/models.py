from scandiKitchen import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

#check if user is authenticated
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#allow user login functions
class User(db.Model,UserMixin):
    #setting up user model
    __tablename__ = 'users'
    #creating unique identification for users
    id = db.Column(db.Integer,primary_key=True)
    #link to a file that user uploads / setting up a default profile image if nothing is submitted
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    #setup email and making sure it is not repeated
    email = db.Column(db.String(64),unique=True,index=True)
    #setup username to be unique
    username = db.Column(db.String(64),unique=True,index=True)
    #setup password for the user using password hashing#
    password_hash = db.Column(db.String(128))

    #connecting recipe with the person who uploaded
    posts = db.relationship('Recipe',backref='author',lazy=True)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}"


class Recipe(db.Model):
    
    users = db.relationship(User)
    #id for each recipie
    id = db.Column(db.Integer,primary_key=True)
    #connect recipie to a user
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    #add published date, title and text
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title = db.Column(db.String(100),nullable=False)
    text = db.Column(db.Text,nullable=False)
    cook_method = db.Column(db.Text,nullable=True)
    ingredients = db.Column(db.Text,nullable=True)
    recipe_image = db.Column(db.String(100),nullable=True)

    def __init__(self,title,text,user_id,cook_method,ingredients,recipe_image):
        self.title = title
        self.text = text
        self.user_id = user_id
        self.cook_method = cook_method
        self.ingredients = ingredients
        self.recipe_image = recipe_image 

    
