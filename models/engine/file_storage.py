#!/usr/bin/python3
"""Module that contains class FileStorage that serializes
instances to a JSON file and deserializes JSON file to instances"""
import json
import models.base_model


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
        self.__objects[str(type(obj).__name__) + "." + str(obj.id)] = obj

    def save(self):
        """ Serializes __objects to the file
        """
        serialized = {}

        for keys, objs in self.__objects.items():
            dict_obj = objs.to_dict()
            serialized[keys] = dict_obj

        json_dictionary = json.dumps(serialized)

        with open(self.__file_path, encoding="UTF", mode="w") as f:
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
            obj = models.base_model.BaseModel(**objs_dict)
            self.__objects[keys] = obj