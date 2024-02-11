#!/usr/bin/python3
"""Module for BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines the common attributes/methods for other classes"""
    def __init__(self, **kwargs):
        """Initialize instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f'
                                )
                        setattr(self, key, value)
            self.id = kwargs.get('id', str(uuid.uuid4()))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Return string representation of BaseModel instance"""
        return f"[{type(self).__name__}] ({self.id}) {str(self.__dict__)}"

    def save(self):
        """Update the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
