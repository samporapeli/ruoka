from flask import url_for
from app import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), unique=True, nullable=False)

    @property
    def url(self):
        return url_for('serve_image_by_uuid', path=self.filename)

    def __repr__(self):
        return '<Image %r>' % self.id
