from flask import render_template,url_for,flash,request,redirect,Blueprint, jsonify
from flask_login import current_user,login_required
from scandiKitchen import db
from scandiKitchen.models import Recipe
from scandiKitchen.recipes.forms import RecipeForm

#register all views as a blueprint in main init.py

recipes = Blueprint('recipes',__name__)

#create a recipe
@recipes.route('/create',methods=['GET','POST'])
@login_required
def create_recipe():
    form = RecipeForm()

    if form.validate_on_submit():

        recipe = Recipe(title=form.title.data,cook_method=form.cook_method.data,text=form.text.data,user_id=current_user.id,ingredients=form.ingredients.data,recipe_image =form.recipe_image.data)
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('core.index'))
    return render_template('create_recipe.html',form=form)

#view recipes
#if correct id entered should leat to correct recipe
#make sure id is a number
@recipes.route('/<int:recipe_id>')
def recipe(recipe_id):
    #if id is incorrect page crashes if 404 is not set
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe.html',title=recipe.title,date=recipe.date,post=recipe)

#Search recipe
@recipes.route('/search/<string:search_word>')
def search(search_word):
    search_results = Recipe.query.filter(Recipe.title.contains(search_word)).all()
    print(search_results)
    return render_template('search.html',recipes=search_results)


#update recipe
@recipes.route('/<int:recipe_id>/update',methods=['GET','POST'])
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
        recipe.cook_method = form.cook_method.data
        recipe.ingredients = form.ingredients.data
        recipe.recipe_image = form.recipe_image.data
        db.session.commit()
        return redirect(url_for('recipes.recipe',recipe_id=recipe.id))
    
    #keep original text prefilled in the form
    elif request.method == 'GET':
        form.title.data = recipe.title
        form.text.data = recipe.text
        form.cook_method.data = recipe.cook_method
        form.ingredients.data = recipe.ingredients
        form.recipe_image .data = recipe.recipe_image

    return render_template('create_recipe.html',title='Updating',form=form)


#delete recipe
#NEED TO ADD A BUTTON FOR DELETION INSTEAD OF SEPARATE TEMPLATE

@recipes.route('/<int:recipe_id>/delete',methods=['GET','POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    if recipe.author != current_user:
        abort(403)

    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('core.index'))
    

# @app.route('/search')
# def search():
#     """Provides logic for search bar"""
#     orig_query = request.args['query']




    # using regular expression setting option for any case

    # query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}
    # # find instances of the entered word in title, tags or ingredients
    # results = mongo.db.recipes.find({
    #     '$or': [
    #         {'title': query},
    #         {'tags': query},
    #         {'ingredients': query},
    #     ]
    # })

    # random_query_result = "whatever"

    # # processing result

    # result = [
    #     {
    #         "title": "x1",
    #         "text": "y1"
    #     },
    #     {
    #         "title": "x2",
    #         "text": "y2"
    #     }
    # ]

    # return jsonify(result)


    
