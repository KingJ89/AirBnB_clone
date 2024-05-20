#!/usr/bin/python3
"""
Module for the FileStorage class.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class for serializing and deserializing objects to/from JSON."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON and writes to file."""
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """Deserializes JSON file to recreate objects."""
        filepath = FileStorage.__file_path
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = key.split('.')[0]
                    if class_name == 'BaseModel':
                        self.__objects[key] = BaseModel(**value)
                    elif class_name == 'User':
                        self.__objects[key] = User(**value)
                    elif class_name == 'Place':
                        self.__objects[key] = Place(**value)
                    elif class_name == 'State':
                        self.__objects[key] = State(**value)
                    elif class_name == 'City':
                        self.__objects[key] = City(**value)
                    elif class_name == 'Amenity':
                        self.__objects[key] = Amenity(**value)
                    elif class_name == 'Review':
                        self.__objects[key] = Review(**value)
