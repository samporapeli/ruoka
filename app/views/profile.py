from flask import abort, render_template, request, session, url_for, redirect

from app import app, db
from app.models.user import User
from app.models.image import Image

@app.route('/u/<string:username>', methods=['GET'])
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    else:
        images = Image.query.filter_by(user=user).all()
        return render_template('profile.html', user=user, images=images)

