#!/usr/bin/python3
"""Module that contains class FileStorage that serializes
instances to a JSON file and deserializes JSON file to instances"""
import json
import models.base_model
import models.user


class FileStorage:
    """ Serializes and deserializes instances to JSON format
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ Sets in __object dictionary an instance <obj classname>.id
        """
        FileStorage.__objects[str(type(obj).__name__) + "." + str
                              (obj.id)] = obj

    def save(self):
        """ Serializes __objects to the file
        """
        serialized = {}

        for keys, objs in FileStorage.__objects.items():
            dict_obj = objs.to_dict()
            serialized[keys] = dict_obj

        json_dictionary = json.dumps(serialized)

        with open(FileStorage.__file_path, encoding="UTF", mode="w") as f:
            f.write(json_dictionary)

    def reload(self):
        """ deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF-8") as f:
                objs_dict_read = f.read()
                new_dict_reloaded = json.loads(objs_dict_read)
        except:
            return

        for keys, objs_dict in new_dict_reloaded.items():
            if "BaseModel" in keys:
                obj = models.base_model.BaseModel(**objs_dict)
            if "User" in keys:
                obj = models.user.User(**objs_dict)
            if "Place" in keys:
                obj = models.place.Place(**objs_dict)
            if "State" in keys:
                obj = models.state.State(**objs_dict)
            if "City" in keys:
                obj = models.city.City(**objs_dict)
            if "Amenity" in keys:
                obj = models.user.Amenity(**objs_dict)
            if "Review" in keys:
                obj = models.review.Review(**objs_dict)
            FileStorage.__objects[keys] = obj
