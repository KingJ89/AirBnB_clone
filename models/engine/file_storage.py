#!/usr/bin/bash/env python3
import json

class FileStorage:
    """Handles serialization and deserialization of instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            for key, obj in FileStorage.__objects.items():
                temp[key] = obj.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            pass

    def get(self, key):
        """Retrieve an object by key."""
        return self.__objects.get(key)

    def delete(self, key):
        """Delete an object by key."""
        if key in self.__objects:
            del self.__objects[key]

