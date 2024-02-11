#!/usr/bin/python3
"""
Module for BaseModel class
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel instance

        Args:
             *args: Variable length argument list
             **kwargs: Arbitrary keyword arguments
        """
        # if kwargs is not empty
        if kwargs:
            # remove "__class__' key from dictionary if present
            kwargs.pop('__class__', None)

            # Convert 'created_at' & 'updated_at' str to datetime object
            created_at_str = kwargs.pop('created_at', None)
            updated_at_str = kwargs.pop('updated_at', None)
            if created_at_str:
                kwargs['created_at'] = datetime.fromisoformat(created_at_str)
            else:
                kwargs['created_at'] = datetime.now()
            if updated_at_str:
                kwargs['updated_at'] = datetime.fromisoformat(updated_at_str)
            else:
                kwargs['updated_at'] = datetime.now()

            # Set attributes based on the dictionary
            for key, value in kwargs.items():
                setattr(self, key, value)
        # If kwargs is empty
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self, storage=None):
        """
        Updates the public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()
        if storage is not None:
            # Check if the instance already has an id
            if not hasattr(self, 'id'):
                # If not, generate a new id
                self.id = str(uuid.uuid4())
            # add the instance to storage
            storage.new(self)

    def to_dict(self):
        """
        Returns a dictionary with all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """
        re-create an instance with this dictionary representation
        """
        # Remove '__class__' key from the dictionary if present
        obj_dict.pop('__class__', None)

        # Convert 'created_at' & 'updated_at' str to datetime object ]
        obj_dict['created_at'] = datetime.fromisoformat(obj_dict['created_at'])
        obj_dict['updated_at'] = datetime.fromisoformat(obj_dict['updated_at'])

        # create a new instance of BaseModel
        new_instance = cls()

        # set attributes based on the dictionary
        for key, value in obj_dict.items():
            setattr(new_instance, key, value)

        return new_instance
