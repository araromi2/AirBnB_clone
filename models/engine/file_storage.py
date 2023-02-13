#!/usr/bin/python3
"""This module contains the FileStorage class"""
import json
from datetime import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            dct = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(dct, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                dct = json.load(f)
               for obj in dct.values():
                    cls_name = obj["__class__"]
                    obj.pop("__class__")
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass

        