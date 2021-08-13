from app import db

collection_image = db.Table('collection_image', db.Model.metadata,
   db.Column('id', db.Integer, primary_key=True),
   db.Column('collection_id', db.Integer, db.ForeignKey('collection.id')),
   db.Column('image_id', db.Integer, db.ForeignKey('image.id')),
)

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.relationship('user',
        backref=db.backref('collections', lazy=True)
    )
    images = db.relationship('image', secondary=collection_image)
    
    def __repr__(self):
        return '<Collection %r>' % self.id
