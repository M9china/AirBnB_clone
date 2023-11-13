#!/usr/bin/python3
"""a classe that inherit from BaseModel"""

from models.basemodel import BaseModel


class Review(BaseModel):
    """Review Class"""
    place_id = ""
    user_id = ""
    text = ""
