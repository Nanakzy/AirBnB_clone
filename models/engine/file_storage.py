#!/usr/bin/python3

import json


class FileStorage:
    """Class serialization and deserialization of objects to/from JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects to JSON file."""
        objects_dict = {}
        for key, obj in FileStorage.__objects.items():
            objects_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Deserialize objects from JSON file."""
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects_dict = json.load(f)
                for key, obj_dict in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_cls = eval(class_name)
                    obj = obj_cls(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
