from flask import render_template, request, abort

from app import app, db
from app.models.image import Image

@app.route('/')
def view_frontpage():
    images = Image.query.order_by(Image.id.desc()).all()
    return render_template('frontpage.html', images=images)
