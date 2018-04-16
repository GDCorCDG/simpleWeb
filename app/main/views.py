from app.main import main
from flask import jsonify,request,flash,render_template,url_for,redirect
from flask_login import login_required

#define route
@main.route('/')
def root():
	return redirect(url_for('main.index'),302)


@main.route('/index')
def index():
	return render_template('index.html')

@main.errorhandler(404)
def not_found(error):
	return "404 not found"

@main.errorhandler(500)
def internall_error(error):
	db.session.rollback()
	return '500 error'