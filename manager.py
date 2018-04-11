from app import app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from app.auth import auth
from app.main import main
from app.api import api

app.register_blueprint(auth,url_prefix = '/auth')
app.register_blueprint(api,url_prefix = '/api')
app.register_blueprint(main)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
	manager.run()
