from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from secret import upload_folder, max_upload_size, secret_key

app = Flask(__name__)
app.secret_key = secret_key

app.config['UPLOAD_FOLDER'] = upload_folder
app.config['MAX_CONTENT_LENGTH'] = max_upload_size

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import controllers

# make get_user globally available
from app.controllers.user import get_user
app.jinja_env.globals.update(get_user=get_user)
