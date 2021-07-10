from flask import render_template

from app import app, db
from app.models.image import Image

@app.route('/')
def view_frontpage():
    images = Image.query.all()
    return render_template('frontpage.html', images=images)
