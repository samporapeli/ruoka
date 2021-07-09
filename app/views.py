from app import app
from flask import render_template, redirect, url_for

@app.route('/')
def view_frontpage():
    return render_template('frontpage.html')

@app.route('/create', methods=['GET'])
def view_create():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def handle_create():
    # TODO: actually save the images
    return redirect(url_for('view_frontpage'))
