from typing import Any
from bson import ObjectId
from app.database.db_conn import db
from app.models.item_model import Item
from datetime import date, datetime

from app.utils.mongo_serializer import serialize_doc, serialize_docs


def create_item(data: dict) -> str:
    item = Item(**data)

    if db.items.find_one({"name": item.name}):
        raise RuntimeError("Item Already Exists !!")

    final_item = {
        "name": item.name,
        "user_name": item.user_name,
        "quantity": item.quantity,
        "category_name": item.category_name,
        "expiry_date": item.expiry_date.isoformat(),
        "added_on": date.today().isoformat(),
        "image_url": item.image_url
    }

    result = db.items.insert_one(final_item)
    return result.inserted_id


def get_all_items() -> list[Any]:
    items = list(db.items.find())

    return serialize_docs(items)


def get_item_by_id(item_id: str) -> Item:
    item = db.items.find_one({"_id": ObjectId(item_id)})

    if not item:
        raise RuntimeError("Item Not Found")

    return serialize_doc(item)


def get_item_by_name(name: str) -> Item:
    item = db.items.find_one({"name": name})

    if not item:
        raise RuntimeError("Item Not Found")

    return serialize_doc(item)


def update_item_by_id(item: Item, item_id: str) -> Item:
    # if username != item.get('user_name'):
    #     raise AuthenticationError("You are not Authenticated to edit this Item")

    item_obj_id = ObjectId(item_id)

    result = db.items.update_one(
        {"_id": item_obj_id},
        {
            "$set": {
                **item,
                "updated_on": datetime.now().isoformat()  # optional
            }
        }
    )

    if result.matched_count == 0:
        raise RuntimeError("Item not found to update.")

    updated_item = db.items.find_one({"_id": item_obj_id})

    return serialize_doc(updated_item)


def delete_item_by_id(item_id: str) -> str:
    result = db.items.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise RuntimeError("Item Not Found or Already Deleted !!")

    return "Item Deleted Successfully !!"