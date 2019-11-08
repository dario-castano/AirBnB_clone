#!/usr/bin/python3
"""Module that contains class FileStorage that serializes
instances to a JSON file and deserializes JSON file to instances"""
import json

class FileStorage:
    """ Serializes and deserializes instances to JSON format
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __object dictionary an instance <obj classname>.id
        """
        FileStorage.__objects[type(obj).__name__ + str(obj.id)] = obj

    def save(self):
        """ Serializes __objects to the file
        """
        serialized = {}

        for keys, objs in FileStorage.__objects:
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
                objs_dict = f.read()
        except:
            return

        FileStorage.__objects = json.loads(objs_dict)
