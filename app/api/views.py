from app.api import api
from flask import jsonify,request,flash,render_template,url_for,redirect
from flask_login import login_required


@api.route('/wip')
@login_required
def remote_ip():
	ip = request.remote_addr
	return jsonify({'remote_ip' : ip})

@api.route('/agent')
@login_required
def user_agent():
	return jsonify({'user-agent':request.headers.get('User-Agent')})

@api.route('/flash')
@login_required
def flash_info():
	flash('success!!!!!')
	return render_template('flash.html'),200