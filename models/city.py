#!/usr/bin/python3
"""
city module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class
    Parent:
        BaseModel
    """

    state_id = ""
    name = ""
