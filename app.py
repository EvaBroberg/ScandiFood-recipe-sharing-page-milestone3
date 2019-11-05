from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cookbook.db'
db = SQLAlchemy(app)

class Cookbook(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.string(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return 'User: {}'.format(name)    

if __name__ == "__main__":
    app.run(debug=True)    