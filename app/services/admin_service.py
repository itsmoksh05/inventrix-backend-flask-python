from typing import Any
from bson import ObjectId
from app.database.db_conn import db
from app.utils.mongo_serializer import serialize_docs, serialize_doc
from app.models.user_model import User


def get_all_users() -> list[Any]:
    users = db.users.find()
    return serialize_docs(users)


def get_user_by_id(user_id: str) -> User:
    user = db.users.find_one({"_id": ObjectId(user_id)})

    if user is None:
        raise RuntimeError("User Not Found !!")

    return serialize_doc(user)


def delete_user_by_id(user_id: str) -> str:
    result = db.users.delete_one({"_id": ObjectId(user_id)})

    if result.deleted_count == 0:
        raise RuntimeError("User Not Found or Already Deleted !!")

    return "User Successfully Deleted !!"
