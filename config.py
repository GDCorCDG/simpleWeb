import os

basedir = os.path.abspath('.')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'database.db')
SECRET_KEY = 'your_secret_key'