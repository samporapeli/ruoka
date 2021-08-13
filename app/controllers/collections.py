from flask import render_template, request, abort

from app import app, db
#from app.models.collections import Collection

@app.route('/notebooks')
def view_collections():
    return render_template('collections.html')
