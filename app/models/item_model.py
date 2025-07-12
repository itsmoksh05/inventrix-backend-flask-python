from typing import Optional
from datetime import date
from pydantic import BaseModel

"""
    Items Model
    {
        name : string -> Item's name
        user_id : string -> Item belongs to which user
        quantity : int = 0 -> Item's Quantity, default is 0
        image_url : string -> optional field for image
        expiry_date : python date -> expiry date for Item
        category_id : string -> Item belongs to which category
        added_on : python date -> Item added on which date 
    }
"""


class Item(BaseModel):
    name: str
    user_name: str
    quantity: int = 0
    image_url: Optional[str] = None
    expiry_date: date
    category_name: str
    added_on: date = date.today()