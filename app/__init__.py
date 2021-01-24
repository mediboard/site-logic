from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app(config_file=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_pyfile(config_file)

	db.init_app(app)
	migrate.init_app(app, db, render_as_batch=True)
	login.init_app(app)

	from app.drugs import bp as drugs_bp
	app.register_blueprint(drugs_bp, url_prefix='/drugs')

	from app.board import bp as board_bp
	app.register_blueprint(board_bp, url_prefix='/board')

	return app
