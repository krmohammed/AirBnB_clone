#!/usr/bin/python3
"""
Storage Engine
"""
import json
import os


class FileStorage:
    """
    Storage Engine
        serializes instances to a JSON file and
        deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        provides the __objects attribute
        Returns:
            the private attribute __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Arguments:
            obj (class): class object
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
            (path: __file_path)
        """
        serialized = {}
        for k, v in FileStorage.__objects.items():
            serialized[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists)
        """
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for k, v in data.items():
                    class_name, obj_id = k.split(".")
                    instance = eval(class_name)(**v)
                    FileStorage.__objects[k] = instance


    def destroy(self, obj_key):
        """
        deletes an instance by key
        """
        if obj_key in FileStorage.__objects:
            del FileStorage.__objects[obj_key]
