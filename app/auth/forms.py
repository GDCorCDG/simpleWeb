from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import  DataRequired,Length

class LoginForm(Form):
	name = StringField('Username',[DataRequired(),Length(max=255)])
	passwd = PasswordField('Passwd',[DataRequired()])
	remember = BooleanField('Remember Me')