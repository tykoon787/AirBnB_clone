#!/usr/bin/python3
import json
import os


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
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Function that serializes the obj dict to a json file
        """
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self): 
        """
        Deserialzes the JSON file to __objects (dictionary)
        """
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, mode="r", encoding="utf-8") as f:
                        read_file = f.read()
                        list_of_instances = json.loads(read_file)
                        self.__objects = list_of_instances                            
            else:
               pass 
        except FileNotFoundError as e:
            pass

