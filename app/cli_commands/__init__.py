import click

from app import app, db
from app.models.user import User

# https://flask.palletsprojects.com/en/2.0.x/cli/#custom-commands

@app.cli.command("add-user")
@click.argument("name")
def add_dummy_users(name):
    db.session.add(User(username=name))
    db.session.commit()
