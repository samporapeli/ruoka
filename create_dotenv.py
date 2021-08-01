import sys
import os
import secrets

cwd = os.getcwd()
filename = '.env'
path = os.path.join(cwd, filename)

if os.path.isfile(path):
    print('{}: .env: File exists'.format(sys.argv[0]))
    exit(1)

print('Creating .env')
with open(path, 'w') as f:

    print('Generating SECRET_KEY')
    secret_key = secrets.token_urlsafe()
    f.write('SECRET_KEY={}\n'.format(secret_key))

    upload_folder = os.path.join(cwd, 'uploads')
    print('Setting UPLOAD_FOLDER path to {}'.format(upload_folder))
    f.write('UPLOAD_FOLDER={}\n'.format(upload_folder))

print('Done.')

