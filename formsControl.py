from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class tickForm(FlaskForm):
    #inicialización de campos
    tickTitle = StringField('Title', validators=[DataRequired()])
    tickDate = DateField('Date:',validators=[DataRequired()])
    submit = SubmitField("start ticking!")