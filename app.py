import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'uploads')

#create sqlalchemy object
db = SQLAlchemy(app)


from models import *

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)


class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
    submit = SubmitField('Upload')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
    else:
        file_url = None
    return render_template('upload.html', form=form, file_url=file_url)


# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('Please log in')
#             return redirect(url_for('login'))
#     return wrap

@app.route('/')
# @login_required
def index():
    return render_template('index.html') 

@app.route('/recipes')
def recipes():
    posts = db.session.query(Recipe).all()
    return render_template('recipes.html', posts=posts) #render a template

@app.route('/login', methods=['GET','POST'])   
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('recipes'))
    return render_template('login.html',error =error) 

@app.route('/logout')
# @login_required
def logout():
    session.pop('logged_in', None)
    flash('You are logged out')
    return redirect(url_for('index'))    

# def connect_db ():
#     return sqlite3.connect(app.database)              

if __name__ == '__main__':
    app.run(debug=True)










# enter in order to run site
# set DATABASE_URL=sqlite:///posts.db