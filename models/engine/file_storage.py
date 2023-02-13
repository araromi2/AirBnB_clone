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
                for key, value in dct.items():
                    FileStorage.__objects[key] = BaseModel.class_from_dict(value)
        except FileNotFoundError:
            return
    @staticmethod
    def class_from_dict(dct):
        """Returns an instance with all attributes already set"""
        if dct.get("__class__") == "BaseModel":
            obj = BaseModel(**dct)
        return obj