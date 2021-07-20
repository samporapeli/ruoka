from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from secret import upload_folder, max_upload_size, secret_key

app = Flask(__name__)
app.secret_key = secret_key

app.config['UPLOAD_FOLDER'] = upload_folder
app.config['MAX_CONTENT_LENGTH'] = max_upload_size

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import views

# make get_user globally available
from app.views.user import get_user
app.jinja_env.globals.update(get_user=get_user)
