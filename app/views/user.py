from app import app, db

from flask import render_template, request, session

@app.route('/me', methods=['GET', 'POST'])
def user():
    #if request.method == 'POST':

    name = session.get('username')

    return render_template('user.html', name=name)
