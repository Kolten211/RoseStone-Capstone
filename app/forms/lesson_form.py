from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LessonFrom(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    difficulty = StringField('Difficulty', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    words = SelectMultipleField('Words', choices=[], validators=[DataRequired()])
    phrases = SelectMultipleField('Phrases', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')