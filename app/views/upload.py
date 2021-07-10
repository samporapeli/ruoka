from random import random
from os import path
from uuid import uuid4

from app import app, db
from flask import render_template, request, redirect, url_for

from app.models.image import Image

def random_filename():
    return str(uuid4())

@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'GET':
        return render_template('upload_image.html')

    # No image uploaded
    if 'image' not in request.files:
        return render_template('upload_image.html')
    file = request.files['image']
    if file.filename == '': 
        return render_template('upload_image.html')

    if file.content_type == 'image/jpeg':
        extension = '.jpeg'
    elif file.content_type == 'image/png':
        extension = '.png'
    else:
        return 'invalid filetype'

    # A valid image is uploaded, save to disk
    filename = random_filename() + extension
    db.session.add(Image(filename=filename))
    db.session.commit()
    file.save(path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect(url_for('view_frontpage'))

@app.route('/list-images')
def list_images():
    images = Image.query.all()
    return render_template('list_images.html', images=images)
