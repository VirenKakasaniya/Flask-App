from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
import email_validator

class LoginForm(FlaskForm):
    sensor_id = StringField('sensor_id', validators=[DataRequired('The id seems incorrect'), Length(min=1,max=30)])
    submit = SubmitField('LOG IN')
