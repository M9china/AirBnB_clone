#!/usr/bin/python3
"""a classe that inherit from BaseModel"""

from models.basemodel import BaseModel


class City(BaseModel):
    """City Class"""
    state_id = ""
    name = ""
