#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes.

    Attributes:
        id (str): A unique identifier for each instance.
        created_at date and time when an instance is created.
        updated_at date & time when an instance is last updated.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Attributes:
            id (str): A unique identifier generated using uuid.
            created_at current date & time when instance is created.
            updated_at current date & time when instance is created.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: contains the class name, id, & dict rep of instance.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """
        Updates the updated_at attribute with the current date and time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: containing all instance attributes with formatting
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
