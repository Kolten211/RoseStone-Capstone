from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired

class PhraseForm(FlaskForm):
    words = SelectMultipleField('Learned Words', choices=[], validators=[DataRequired()])
    phrase = StringField('Phrase', validators=[DataRequired()])
    submit = SubmitField('Create Phrase')