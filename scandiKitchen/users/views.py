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



#user account update (post view)
@users.route('/account',methods=['GET','POST'])
#require to be logged in in order to update posts
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        #check if there is any picture uploaded link it to username and update
        #all picture handling will take place in pictures.py after upload
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data,username)
            current_user.profile_image = pic
        #enable email and username update
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('users.account'))
    #if nothing is submitted old email and username is used
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    #take image and render it to the account page
    profile_image = url_for('static',filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html',profile_image=profile_image,form=form)

#recipes views
@users.route('/<username>')
def user_posts(username):
    #go through user posts using pages
    page = request.args.get('page',1,type=int)
    #take a user or if user puts in username incorrectly goes to 404
    user = User.query.filter_by(username=username).first_or_404()
    #take all recipes associate with user and sort by date, display 5 recipes per page
    recipes = Recipe.query.filter_by(author=user).order_by(Recipe.date.desc()).paginate(page=page,per_page=5)
    #pass recipes to users template 
    return render_template('user_recipes.html',recipes=recipes,user=user)


