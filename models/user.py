#!/usr/bin/python3
"""Module that contains class User that
inherits from base models"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class for Users instances
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
