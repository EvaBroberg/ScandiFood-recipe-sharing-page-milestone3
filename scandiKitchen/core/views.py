from scandiKitchen.models import Recipe
from flask import render_template,request,Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():
    #set up to display recipes
    page = request.args.get('page',1,type=int)
    #display recipes in descending order by date
    recipes = Recipe.query.order_by(Recipe.date.desc()).paginate(page=page,per_page=15)
    return render_template('index.html',recipes=recipes)

@core.route('/info') 
def info():
    return render_template('info.html')   