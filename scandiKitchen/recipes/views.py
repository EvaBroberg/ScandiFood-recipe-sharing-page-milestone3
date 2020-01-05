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

#update recipe
@recipe.route('/<int:recipe_id/update>',methods=['GET','POST'])
@login_required
def update(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    #make sure that author of recipe is the same as the user who is logged in
    #if user isn't the author they get 403 error forbiden to edit
    if recipe.author != current_user:
        abort(403)

    form = RecipeForm()

    if form.validate_on_submit():
        #reset title and text to the title in the form
        #commit changes to data base
        #redirecting user to updated recipe
        recipe.title = form.title.data
        recipe.text = form.text.data
        db.session.commit()
        return redirect(url_for('user_recipes.recipe',recipe_id = recipe.id))
    
    #keep original text prefilled in the form
    elif request.method = 'GET':
        form.title.data = recipe.title
        form.text.data = recipe.text

    return render_template('create_recipe.html',title='Updating',form=form)


#delete recipe
#NEED TO ADD A BUTTON FOR DELETION INSTEAD OF SEPARATE TEMPLATE

@recipe.route('/<int:recipe_id/delete>',methods=['GET','POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    if recipe.author != current_user:
        abort(403)

    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('core.index'))
    



    
