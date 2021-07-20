from flask import render_template, request, redirect, abort, url_for

from app import app, db
from app.views.image_uploads import save_uploaded_image
from app.views.user import get_user

# handle upload and redirect user to frontpage
@app.route('/', methods=['POST'])
def handle_upload():
    user = get_user()
    if 'image' in request.files:
        file = request.files['image']
        if user is None:
            abort(403)
        save_uploaded_image(file, user=user)
        return redirect(url_for('view_frontpage'))
    else:
        abort(400)  # bad request
