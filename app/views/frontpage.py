from app import app, db
from flask import render_template

@app.route('/')
def view_frontpage():
    return render_template('frontpage.html')
