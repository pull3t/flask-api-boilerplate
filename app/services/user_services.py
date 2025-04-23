### --- flask-boilerplate/app/routes/user_service.py ---
from app.models.user import User
from app.extensions import db
from sqlalchemy.exc import IntegrityError

def create_user(username):
    new_user = User(username=username)
    db.session.add(new_user)
    try:
        db.session.commit()
        return new_user
    except IntegrityError:
        db.session.rollback()
        raise ValueError("Username already exists")

def get_user(user_id):
    return User.query.get(user_id)

def get_all_users():
    return User.query.all()

def update_user(user_id, new_username):
    user = User.query.get(user_id)
    if not user:
        return None
    user.username = new_username
    try:
        db.session.commit()
        return user
    except IntegrityError:
        db.session.rollback()
        raise ValueError("Username already exists")

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return False
    db.session.delete(user)
    db.session.commit()
    return True
