from app.auth import auth
from app import lm
from ..models import User
from .forms import LoginForm
from flask import jsonify,request,flash,render_template,url_for,redirect
from flask_login import login_user,logout_user,login_required


@lm.user_loader
def load_user(userid):
	return User.query.filter_by(id = userid).first()

#define route
@auth.route('/login',methods = ['GET','POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			username = request.form['name']
			password = request.form['passwd']
			user = User.query.filter_by(name = username).first()
			if not  user or not user.verify_passwd(password):
				return "Invalid username or password!"
			login_user(user,remember=form.remember.data)
			print "logining .............."
			return render_template("auth/hello.html")
		return render_template('auth/login.html', form=form)
	if request.method == 'GET':
		return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.index'),302)



