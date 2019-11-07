#!/usr/bin/python3
"""Module that contains class BaseModel that defines all
common attributes/methods for other classes"""
import datetime
import uuid

class BaseModel:
    """ Base model for all other classes
    """
    def __init__(self):
        """ Constructor method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """New str representation for the class
        """
        return "[" + type(self).__name__ + "] " + "(" + self.id + ") " + str(self.__dict__)

    def save(self):
        """ Updates the public instance attribute Updated at
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict[__class__] = type(self).__name__
        return new_dict
