# ruoka

## set up development environment
```zsh
git clone git@github.com:samporapeli/ruoka.git
cd ruoka
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
# create .env file as described below
flask db upgrade
python init_db.dev.py
flask run
```

## create `.env` configuration file
- `SECRET_KEY` with a cryptographically secure random token. Can be generated with the command below:
    - `python3 -c 'import secrets; print(secrets.token_urlsafe())'`
- `UPLOAD_FOLDER` with absolute directory path
- You can also override any values present in `.flaskenv`

Example content of `.env`:

```
SECRET_KEY=r09cBDUkXjMUG5-wgBUdw-1CppFZsF2Dcrt6bDpYoCU # just generate one yourself and don't use this
UPLOAD_FOLDER='/home/user/Projects/ruoka/uploads'
```
