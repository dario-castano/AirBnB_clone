#!/usr/bin/python3
""" Module that contains the class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ New class City that inherits from BaseModel and contains the cities
    """
    state_id = ""
    name = ""
