import click

from app import app, db
from app.models.user import User

# https://flask.palletsprojects.com/en/2.0.x/cli/#custom-commands

def add_user(name):
    db.session.add(User(username=name))
    db.session.commit()

@app.cli.command("add-user")
@click.argument("name")
def cli_add_dummy(name):
    add_user(name)

@app.cli.command("populate-dev-db")
def cli_populate_dev_db():
    add_user('devuser1')
    add_user('devuser2')
    add_user('devuser3')
