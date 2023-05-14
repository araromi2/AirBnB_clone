#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class handles serialization and desierialization
    of object to/from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objectdd.

        Returns:
            dict: Dictionary of objects stored in __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets the object in __objects with the key <obj class name>.id.

        Args:
            obj (BasModel): The object to be stored.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for value in data.values():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            return
