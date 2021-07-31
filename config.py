from secret import upload_folder, max_upload_size, secret_key

class Config:
    SECRET_KEY = secret_key

    UPLOAD_FOLDER = upload_folder
    MAX_CONTENT_LENGTH = max_upload_size

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
