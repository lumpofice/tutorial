from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired

class IntegerInputForm(FlaskForm):
    integer = IntegerField('Integer', validators=[InputRequired()])
    submit = SubmitField('Run')
