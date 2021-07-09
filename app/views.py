from random import random

from app import app, db
from flask import render_template, redirect, url_for

from app.models.image import Image

@app.route('/')
def view_frontpage():
    return render_template('frontpage.html')

@app.route('/create', methods=['GET'])
def view_create():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def handle_create():
    # TODO: actually save the images
    return redirect(url_for('view_frontpage'))

@app.route('/list-images')
def list_images():
    images = Image.query.all()
    return render_template('list_images.html', images=images)

@app.route('/add-image')
def add_image():
    filename = str(random())
    db.session.add(Image(filename=filename))
    db.session.commit()
    return list_images()
