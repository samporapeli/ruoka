from flask import render_template, request, abort

from app import app, db
from app.models.image import Image

@app.route('/image-info/<int:image_id>')
def image_info(image_id):
    image = Image.query.filter_by(id=image_id).first()
    if image is None:
        abort(404)
    return render_template('image_info.html', image=image)
