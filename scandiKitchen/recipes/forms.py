from flask_wtf import FlaskForm
from wtforms import StringField,Submitfield,TextAreaField
from wtforms.validators import DataRequired

class RecipeForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    text = TextArea('Text',validators=[DataRequired()])
    submit = SubmitField()