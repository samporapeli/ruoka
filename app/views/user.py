from flask import render_template, request, session

from app import app, db
from app.models.user import User

def get_user():
    return session.get('user')

@app.route('/me', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        new_user = request.form.get('user')
        session['user'] = int(new_user)

    users = User.query.all()
    current_user = get_user()

    return render_template('user.html', users=users, current_user_id=current_user)
