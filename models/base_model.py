#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage
"""
This module contains the Base Class

Classes:
    BaseModel()

Functions:
    __int__(self, args, kwargs)
    __str__(self)
    save(self)
    to_dict(self)

Misc Variables:
    storage
"""


class BaseModel():
    date_time_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        if (len(kwargs) != 0):
            print("Key words args found")
            for key, value in kwargs.items():
                print("Key: {} Value {}".format(key, value))
                if key != "__class__":
                    if key == "created_at":
                        datetime.strptime(value, self.date_time_format)
                    if key == "updated_at":
                        datetime.strptime(value, self.date_time_format)
                    setattr(self, key, value)
        else:
            print("Entring Else statement")
            self.id = uuid4()
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        Function taht updates the public instance
        attribute `updated at` with the current date and time
        """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Function that returns a dict rep of an instance
        """
        final_dict = {}
        key = "__class__"
        value = self.__class__.__name__
        final_dict[key] = value
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                final_dict[key] = value.isoformat()
            elif key == "id":
                final_dict[key] = str(value)
            else:
                final_dict[key] = value
        return (final_dict)
