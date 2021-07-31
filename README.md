# ruoka

## set up development environment
```zsh
git clone git@github.com:samporapeli/ruoka.git
cd ruoka
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
# create a secret.py as described below
flask db upgrade
python init_db.dev.py
flask run
```

## create `secret.py` configuration file
`secret.py` is a configuration file that contains instance specific configuration.
It should not be stored in version control system, as `secret_key` must not be shared.

- `upload_folder` (str) with absolute directory path
- `max_upload_size` (int), for example 100 million for 100MB
- `secret_key` (str) with a cryptographically secure random token. Can be generated with the command below:
    - `python3 -c 'import secrets; print(secrets.token_urlsafe())'`
- `debug` (bool)

Example content of `secret.py`:

```python3
upload_folder = '/home/user/Projects/ruoka/uploads'
max_upload_size = 100000000
secret_key = 'r09cBDUkXjMUG5-wgBUdw-1CppFZsF2Dcrt6bDpYoCU' # just generate one yourself and don't use this
debug = True # set to False in production
```
