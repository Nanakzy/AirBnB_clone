#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:
    """
    Handles serialization and deserialization of instances to/from a JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"
        Returns:
        dict: A dictionary containing all objects currently loaded
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of objects.

        Args:
        obj: The object to add.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes objects to the JSON file
        """
        serialized_objs = {}
        for key, value in self.__objects.items():
            serialized_objs[key] = value.to_dict()
        try:
            with open(FileStorage.__file_path, 'w') as f:
                json.dump(serialized_objs, f)
        except FileNotFoundError:
            # Handle file not found error
            pass
        except json.JSONDecodeError:
            # Handle JSON serialization error
            pass

    def reload(self):
        """
        Deserializes the JSON file and reloads objects into the dictionary.
        """
        self.__objects = {}
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = BaseModel.from_dict(value)
        except FileNotFoundError:
            pass
        return self.__objects
