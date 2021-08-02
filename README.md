# ruoka

## set up development environment
```zsh
git clone git@github.com:samporapeli/ruoka.git
cd ruoka
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python create_dotenv.py
# edit .env and .flaskenv if you want
flask db upgrade
flask add-user dummy1
flask run
```
