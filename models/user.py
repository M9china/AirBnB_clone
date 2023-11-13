#!/usr/bin/python3
"""a class User that inherits from BaseModel"""

from models.basemodel import BaseModel


class User(BaseModel):
    """
    User Class containing class attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
