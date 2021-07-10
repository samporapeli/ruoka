from random import random
from os import path
from uuid import uuid4

from app import app, db
from flask import render_template, request, redirect, url_for, send_from_directory, abort

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

# This is similar to how Nginx would serve the static images if we
# want to do that at some point.

@app.route('/images/<path:path>')
def serve_image(path):
    return send_from_directory(app.config['UPLOAD_FOLDER'], path)

# A more human-readable url with the image's counter id
@app.route('/images/<int:id>')
def serve_image(id):
    image = Image.query.filter_by(id=id).first()
    if image is None:
        abort(404)
    return send_from_directory(app.config['UPLOAD_FOLDER'], image.filename)

@app.route('/list-images')
def list_images():
    images = Image.query.all()
    return render_template('list_images.html', images=images)
