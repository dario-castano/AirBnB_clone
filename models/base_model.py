#!/usr/bin/python3
"""Module that contains class BaseModel that defines all
common attributes/methods for other classes"""
import datetime
import uuid
from models import storage

class BaseModel:
    """ Base model for all other classes
    """
    def __init__(self, *args, **kwargs):
        """ Constructor method
        """
        if kwargs is None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new()
            return

        if "id" in kwargs.keys():
            try:
                uuid.UUID(kwargs["id"])
                self.id = kwargs["id"]
            except:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())

        if ("created_at" in kwargs.keys()):
            self.created_at = datetime.datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.datetime.now()

        if ("updated_at" in kwargs.keys()):
            self.updated_at = datetime.datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.updated_at = datetime.datetime.now()

        for key, value in kwargs.items():
            if (key != "id" and key != "created_at" and key != "updated_at" and key != "__class__"):
                setattr(self, key, value)

    def __str__(self):
        """New str representation for the class
        """
        return "[" + type(self).__name__ + "] " + "(" + self.id + ") " + str(self.__dict__)

    def save(self):
        """ Updates the public instance attribute Updated at
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['__class__'] = type(self).__name__
        return new_dict
