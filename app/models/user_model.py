from pydantic import BaseModel, EmailStr
from app.constants.roles import Roles

"""
    User Model
    {
        name : string -> username
        email : pydantic EmailStr -> User's email
        password : string -> User's Hashed Password
        role : Roles -> Role of User (ADMIN / USER)
    }
"""

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Roles