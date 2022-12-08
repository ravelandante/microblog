from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username is required')])
    password = PasswordField('Password', validators=[DataRequired(message='Password is required')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')