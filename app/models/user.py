### --- flask-boilerplate/app/models/user.py ---
import uuid
from ..extensions import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"