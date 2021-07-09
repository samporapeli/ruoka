from flask import Flask
from secret import upload_folder, max_upload_size

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_folder
app.config['MAX_CONTENT_LENGTH'] = max_upload_size

from app import views
