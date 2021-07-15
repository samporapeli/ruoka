from app import db
from app.models.image import Image
from app.models.user import User

db.create_all()

db.session.add(User(username='devuser1'))
db.session.add(User(username='devuser2'))
db.session.add(User(username='devuser3'))

db.session.commit()
