#!/usr/bin/python3
"""Module for FileStorage class"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        serializable_dict = {key: obj.to_dict()
                             for key, obj in self.__objects.items()}
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serializable_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
                for key, value in FileStorage.__objects.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    class_type = self.__class_map.get(class_name)
                    if class_type:
                        FileStorage.__objects[key] = class_type(**value)
                    else:
                        print(f"Warning: Class '{class_name}' not found.")
        except FileNotFoundError:
            pass
