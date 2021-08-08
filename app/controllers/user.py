from flask import render_template, request, session, url_for, redirect

from app import app, db
from app.models.user import User

def get_user():
    user_id = session.get('user')
    return User.query.filter_by(id=user_id).first()

@app.route('/settings', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        new_user = request.form.get('user')
        session['user'] = int(new_user)
        return redirect(url_for('view_frontpage'))

    users = User.query.all()
    current_user = get_user()

    return render_template('user.html', users=users, current_user=current_user)
