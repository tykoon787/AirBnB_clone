#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

"""
This module contains the file Storage Logic

Claseses:
    FileStorage

Functions:
    all (self)
    new (self)
    save (self)
    reload
"""


class FileStorage():
    """
    File Storage Class
    ....
    Attributes
    ----------
    file_path: String
    objects: dictionary

    ....
    Methods
    -------

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Function that returns the dictonary objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Function that sets in objects dictionary the obj key
        with <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Function that serializes the obj dict to a json file
        """
        serialize_dict = {}
        for key, obj in self.__objects.items():
            print("Save key{} save value{}".format(key, obj))
            serialize_dict[key] = obj.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(serialize_dict, f, indent=4)

    def reload(self):
        """
        Deserialzes the JSON file to __objects (dictionary)
        """
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, mode="r", encoding="utf-8") as f:
                    read_file = f.read()
                    self.__objects = json.loads(read_file)
                    for key, val in self.__objects.items():
                        class_name = val["__class__"]
                        # module_name = "BaseModel"
                        # class_ = getattr(module_name, class_name)
                        class_ = globals()[class_name]
                        obj = class_(**val)
                        self.all()[key] = obj
            else:
                pass
        except FileNotFoundError as e:
            pass
