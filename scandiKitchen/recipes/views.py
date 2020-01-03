from flask import render_template,url_for,request,flash,redirect,Blueprint
from flask_login import current_user,login_required
from scandiKitchen import db
from scandiKitchen.models import BlogPost
from scandiKitchen.recipes.forms import RecipeForm

#register all views as a blueprint in main init.py

recipes = Blueprint('recipes',__name__)

#create a recipe
@recipes.route('/create',methods=['GET','POST'])
@login_required
def create_recipe():
    form = RecipeForm()

    if form.validate_on_submit():
        recipe = Recipe(title=form.title.data,text=form.data,user_id=current_user.id)
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('core.index'))
    return render_template('create_recipe.html'form=form)

#view blogposts
#if correct id entered should leat to correct recipe
#make sure id is a number
@recipes.route('/<int:recipe_id>')
def recipe(recipe_id):
    #if id is incorrect page crashes if 404 is not set
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe.html',title=recipe.title,date=recipe.date,post=recipe)

