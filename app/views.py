from app import app,lm
from .models import User
from .forms import LoginForm
from flask import jsonify,request,flash,render_template,url_for,redirect
from flask_login import login_user,logout_user,login_required

@lm.user_loader
def load_user(userid):
	return User.query.filter_by(id = userid).first()

#define route
@app.route('/')
def root():
	return redirect(url_for('index'),302)

@app.route('/login',methods = ['GET','POST'])
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
			return render_template("hello.html")
		return render_template('login.html', form=form)
	if request.method == 'GET':
		return render_template('login.html', form=form)


@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/wip')
@login_required
def remote_ip():
	ip = request.remote_addr
	return jsonify({'remote_ip' : ip})

@app.route('/agent')
@login_required
def user_agent():
	return jsonify({'user-agent':request.headers.get('User-Agent')})

@app.route('/flash')
@login_required
def flash_info():
	flash('success!!!!!')
	return render_template('flash.html'),200

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'),302)


@app.errorhandler(404)
def not_found(error):
	return "404 not found"


