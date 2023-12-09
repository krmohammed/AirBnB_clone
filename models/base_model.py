#!/usr/bin/python3
"""
base_model module
"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    The BaseModel class
    parent class for all other models
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes public instance attributes

        Args:
            self (instance): instance of the class
            args (tuple): non-keyworded argument
            kwargs (dict): keyworded argument
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        Saves the changes to a JSON file
        """
        self.updated_at = datetime.now()
        storage.save()


    def to_dict(self):
        """
        creates a dict

        Returns:
            a dictionary containing all keys/values
            of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy


    def __str__(self):
        """informal string representation of `self
        """

        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
