# ruoka

## set up development environment
```zsh
git clone git@github.com:samporapeli/ruoka.git
cd ruoka
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python init_db.dev.py
python ruoka.py
```

## create `secret.py`
- `upload_folder` (str) with absolute path
- `max_upload_size` (int), for example 100 million for 100MB
- `secret_key` (str) with a cryptographically secure random token
- `port` (int), for example `3000`
- `debug` (bool) for example `True`
