from flask import Flask
from secret import upload_folder

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_folder

from app import views
