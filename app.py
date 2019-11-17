from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from functools import wraps
import sqlite3

app = Flask(__name__)

app.secret_key = "super secret key"
app.database = "scandi.db"



def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please log in')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def index():
    # g.db = connect_db()
    # cur = g.db.execute('select * from posts')
    # posts = [dict(title=row[0], description = row[1]) for row in cur.fetchall()]
    # g.db.close()
    return render_template('index.html') 

@app.route('/recipes')
def recipes():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description = row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('recipes.html', posts=posts) 

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
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You are logged out')
    return redirect(url_for('index'))    

def connect_db ():
    return sqlite3.connect(app.database)              

if __name__ == '__main__':
    app.run(debug=True)

