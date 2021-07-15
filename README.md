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
