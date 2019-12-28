from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from scandiKitchen import db
from scandiKitchen.models import User,Recipe
from scandiKitchen.users.forms import RegistrationForm,LoginForm,UpdateUserForm
from scandiKitchen.users.pictures import add_profile_pic

users = Blueprint('users',__name__)

#registration view setup
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        #add user to database
        db.session.add(user)
        db.session.commit()
        flash('Welcom to our kitchen!')
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)

#login view setup
@users.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    #query user that already exists and filter by email
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        #check that user provided correct password
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Welcome back! Let's get cooking!")
            #if user tries to access some place and are prompted to login this should keep them in the same place after login
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html',form=form)



#logout view setup
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))