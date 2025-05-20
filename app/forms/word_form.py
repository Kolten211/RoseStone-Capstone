from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired
from wtforms import SubmitField, StringField
from app.api.aws_helper import ALLOWED_EXTENSIONS

class WordForm(FlaskForm):
    word = StringField("Word", validators=[DataRequired()])
    source_language = StringField("Source language")
    target_language = StringField("Target Language")
    image = FileField("Image", validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    submit = SubmitField("Create Word")