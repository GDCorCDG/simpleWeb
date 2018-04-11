from app import db
from datetime import datetime
from werkzeug.security import  generate_password_hash,check_password_hash

class User(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(64),unique = True)
	email = db.Column(db.String(128),unique = True)
	passwd_hash = db.Column(db.String(128))
	create_at = db.Column(db.DateTime)
	role_id = db.Column(db.Integer,db.ForeignKey('role.id'))


	@property
	def is_active(self):
		return True

	@property
	def is_authenticated(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	@property
	def passwd(self):
		raise AttributeError('password is not a readable attribute')

	@passwd.setter
	def passwd(self,password):
		self.passwd_hash = generate_password_hash(password)

	def verify_passwd(self,password):
		return check_password_hash(self.passwd_hash,password)

	# def __init__(self,name,mail,role,create_at = None):
	# 	self.name = name
	# 	self.mail = mail
	# 	self.role = role
	# 	if create_at is None:
	# 		create_at = datetime.utcnow()
	# 	self.create_at = create_at

	def __repr__(self):
		return "<User %r>" % self.name

class Role(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(64),unique = True)
	users = db.relationship('User', backref=db.backref('role'), lazy='dynamic', uselist=True)

	# def __init__(self,name):
	# 	self.name = name

	def __repr__(self):
		return "<Role %r>" % self.name