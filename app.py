from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/recipes')
def recipes():
    return render_template('recipes.html') 

@app.route('/contact')
def contact():
    return render_template('contact.html') 
    
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name) 
 
@app.route('/my_recipes')
def my_recipes():
    return render_template('my_recipes.html') 

@app.route('/my_favourites')
def my_favourites():
    return render_template('my_favourites.html')    

@app.route('/new_recipe')
def new_recipe():
    return render_template('new_recipe.html')

@app.route('/recipe/<recipe_name>')
def recipe(recipe_name):
    return render_template('recipe.html', recipe_name = recipe_name)           

if __name__ == '__main__':
    app.run(debug=True)

