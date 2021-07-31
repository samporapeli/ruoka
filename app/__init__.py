from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import controllers
from app import cli_commands

# make get_user globally available
from app.controllers.user import get_user
app.jinja_env.globals.update(get_user=get_user)
