#!/usr/bin/python3
"""Functional test cases for the BaseModel class."""

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialization of BaseModel Class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """Returns the string representation of an instance"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self) -> None:
        """Update the public instance updated_at"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self) -> dict:
        """Returns the dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        for k, v in obj_dict.items():
            if isinstance(v, datetime):
                obj_dict[k] = v.isoformat()
        return obj_dict
