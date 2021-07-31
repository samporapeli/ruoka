import os

def env_or_exit(name):
    value = os.environ.get(name)
    if not value:
        exit('{} is not set'.format(name))
    return value

class Config:
    SECRET_KEY = env_or_exit('SECRET_KEY')

    UPLOAD_FOLDER = env_or_exit('UPLOAD_FOLDER')
    MAX_CONTENT_LENGTH = env_or_exit('MAX_UPLOAD_SIZE')

    SQLALCHEMY_DATABASE_URI = env_or_exit('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
