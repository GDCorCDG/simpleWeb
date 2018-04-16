from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,ValidationError
from wtforms.validators import  DataRequired,Length,Regexp,Email,EqualTo,Required
from ..models import User

class LoginForm(Form):
	name = StringField('Username',[DataRequired(),Length(max=255)])
	passwd = PasswordField('Passwd',[DataRequired()])
	remember = BooleanField('Remember Me')

class RegisForm(Form):
	name = StringField('UserName',validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
	                                                                         'Usernames must have only latters.'
	                                                                         'numbers,dots or undersores')])
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	passwd = PasswordField('Password',validators=[Required(),EqualTo('passwd2',message='Password must match.')])
	passwd2 = PasswordField('Confirm password',validators=[Required()])

	def validate_email(self,field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

	def validate_username(self,field):
		if User.query.filter_by(name=field.data).first():
			raise ValidationError('User already in use.')