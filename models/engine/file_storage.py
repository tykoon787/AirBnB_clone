#!/usr/bin/python3
import json
import os
import models.base_model as bm
import models.user as user
import models.amenity as amenity
import models.city as city
import models.place as place
import models.review as review
import models.state as state

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
    class_dict = {"BaseModel": bm.BaseModel,
                  "User": user.User,
                  "State": state.State,
                  "Amenity": amenity.Amenity,
                  "Place": place.Place,
                  "Review": review.Review,
                  "City": city.City}
   
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
        print("Self.__objects dictionary: {}".format(self.__objects))
        for key, obj in self.__objects.items():
            print("Save key ===> {} save value ===> {} of type ===> {}".format(key, obj, type(obj)))
            if (isinstance(obj, bm.BaseModel)) or (isinstance(obj, user.User)):
                serialize_dict[key] = obj.to_dict()
            else:
                pass
        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(serialize_dict, f, indent = 4)

    def reload(self): 
        """
        Deserialzes the JSON file to __objects (dictionary)
        """
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, mode="r", encoding="utf-8") as f:
                        read_file = f.read()
                        self.__objects = json.loads(read_file)
                        print("Dictionary after reloading {}".format(self.__objects))
                        for key, value in self.__objects.items():
                            self.__objects[key] = self.class_dict[value["__class__"]](**value)
            else:
               pass 
        except FileNotFoundError as e:
            pass

