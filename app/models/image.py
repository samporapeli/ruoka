from app import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<Image %r>' % self.id
