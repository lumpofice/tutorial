from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class IntegerInputForm(FlaskForm):
    integer = IntegerField('Integer', validators=[InputRequired(), NumberRange(-75, 75)])
    count = IntegerField('Count', validators=[InputRequired(), NumberRange(1, 19)])
    submit = SubmitField('Run')
