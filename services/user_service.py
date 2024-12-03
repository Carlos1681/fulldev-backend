from models.user import User
from extensions.extensions import db

def create_user(username, email, password):
    if User.query.filter_by(email=email).first():
        raise ValueError("Email já cadastrado")
    
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        raise ValueError("Usuário não encontrado")
    return user

def get_all_users():
    return User.query.all()

def delete_user(user_id):
    user = get_user_by_id(user_id)
    db.session.delete(user)
    db.session.commit()