from pymongo.errors import DuplicateKeyError
from app.database.db_conn import db
from app.models.user_model import User
from app.utils.password_util import hash_password, verify_password


def create_user(data: dict) -> str:
    user = User(**data)

    if db.users.find_one({"username": user.username}):
        raise DuplicateKeyError("Username Already Exists !!")

    if db.users.find_one({"email": user.email}):
        raise DuplicateKeyError("Email Already Exists !!")

    hashed_password = hash_password(password=user.password)

    final_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
        "role": user.role.value
    }

    result = db.users.insert_one(final_user)
    return result.inserted_id



def verify_user(username: str, password: str) -> bool:
    user = db.users.find_one({"username": username})

    if not user:
        raise RuntimeError("User Not Found !!")

    if verify_password(user.get('password'), password):
        # return jwt token here
        return True

    raise RuntimeError("Login Failed !!")

""" 
    !!! TO BE AUTHENTICATED !!! 
"""
def get_my_profile(username: str) -> User:

    user = db.users.find_one({"username": username})

    if not user:
        raise RuntimeError("User Not Found !!")

    return user