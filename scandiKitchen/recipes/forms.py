from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,FileField
from wtforms.validators import DataRequired

class RecipeForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    text = TextAreaField('Text',validators=[DataRequired()])
    recipe_image = FileField('Image')
    submit = SubmitField('Post')

    