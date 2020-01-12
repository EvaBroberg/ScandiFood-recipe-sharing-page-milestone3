from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,FileField
from wtforms.validators import DataRequired,Regexp

class RecipeForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    text = TextAreaField('About recipe',validators=[DataRequired()])
    cook_method = TextAreaField('Cooking method',validators=[DataRequired()])
    ingredients = TextAreaField('Ingrediants',validators=[DataRequired()])
    recipe_image = StringField('URL*', validators=[DataRequired('URL is required'),Regexp('^(http|https):\/\/[\w.\-]+(\.[\w.\-]+)+.*$', 0,
'URL must be a valid link')])
    submit = SubmitField('Post')

    