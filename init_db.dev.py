from app import db
from app.models.user import User

db.session.add(User(username='devuser1'))
db.session.add(User(username='devuser2'))
db.session.add(User(username='devuser3'))

db.session.commit()
