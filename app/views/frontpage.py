from flask import render_template, request, abort

from app import app, db
from app.views.image_uploads import save_uploaded_image
from app.views.user import get_user
from app.models.image import Image

@app.route('/', methods=['GET', 'POST'])
def view_frontpage():
    user = get_user()
    if request.method == 'POST':
        if 'image' in request.files:
            file = request.files['image']
            if user is None:
                abort(403)
            save_uploaded_image(file, user=user)

    images = Image.query.order_by(Image.id.desc()).all()
    return render_template('frontpage.html', images=images, user=user)
