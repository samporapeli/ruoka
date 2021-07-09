from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from secret import upload_folder, max_upload_size

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = upload_folder
app.config['MAX_CONTENT_LENGTH'] = max_upload_size

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import views
