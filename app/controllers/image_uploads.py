from random import random
import os
from uuid import uuid4

from flask import render_template, request, redirect, url_for, send_from_directory, abort
import PIL.Image

from app import app, db
from app.models.image import Image
from app.controllers.user import get_user

def random_filename():
    return str(uuid4())

# 1536 = 1.5 * 1024
def create_thumbnail(image, max_side_length=1536):
    width, height = image.size

    multiplier = max_side_length / max(width, height)
    multiplier = min(1, multiplier) # don't enlarge image
    new_size = (width * multiplier, height * multiplier)

    image.thumbnail(new_size)
    return image



def save_uploaded_image(file, user):
    if file.filename == '': 
        return False

    # Check file type
    if file.content_type == 'image/jpeg':
        extension = '.jpeg'
        image_format = 'jpeg'
    elif file.content_type == 'image/png':
        # convert PNGs to JPEGs
        extension = '.jpeg'
        image_format = 'jpeg'
    else:
        abort(403) # other filetypes are not allowed to be saved

    # Check image mode
    image = PIL.Image.open(file)
    if image.mode == 'RGB':
        pass
    elif image.mode == 'RGBA':
        background_color = (255, 255, 255)
        new = PIL.Image.new('RGB', image.size, background_color)
        new.paste(image, mask=image.split()[-1])
        image = new
    else:
        abort(400) # not sure what these formats could be

    image = create_thumbnail(image)

    # A valid image is uploaded, save to disk
    filename = random_filename() + extension
    db.session.add(Image(filename=filename, user_id=user.id))
    db.session.commit()
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(save_path, 'w') as f:
        image.save(f, image_format)

    return True



# Image deletion
@app.route('/delete-image', methods=['POST'])
def delete_image():
    user = get_user()
    image_id = request.form.get('image-id')
    image = Image.query.filter_by(id=image_id).first()
    if not image:
        abort(404)
    if user != image.user:
        abort(403)

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    try:
        os.remove(image_path)
    except FileNotFoundError:
        pass

    db.session.delete(image)
    db.session.commit()

    return redirect(url_for('view_frontpage'))



# This is similar to how Nginx would serve the static images if we
# want to do that at some point.

@app.route('/images/<path:path>')
def serve_image_by_uuid(path):
    return send_from_directory(app.config['UPLOAD_FOLDER'], path)



# A more human-readable url with the image's counter id

@app.route('/images/<int:id>')
def serve_image_by_counter_id(id):
    image = Image.query.filter_by(id=id).first()
    if image is None:
        abort(404)
    return send_from_directory(app.config['UPLOAD_FOLDER'], image.filename)
