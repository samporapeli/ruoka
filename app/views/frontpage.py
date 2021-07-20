from flask import render_template, request, abort

from app import app, db
from app.views.user import get_user
from app.models.image import Image

@app.route('/', methods=['GET'])
def view_frontpage():
    user = get_user()
    images = Image.query.order_by(Image.id.desc()).all()
    return render_template('frontpage.html', images=images, user=user)
