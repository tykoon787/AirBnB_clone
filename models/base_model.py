#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel():
    def __init__(self, *args, **kwargs): 
        date_time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if (len(kwargs) != 0):
            print("Key words args found")
            for key, value in kwargs.items():
                print("Key: {} Value {}".format(key, value))
                if key != "__class__":
                    if key == "created_at":
                        print("Created at found")
                        datetime_obj = datetime.strptime(value, date_time_format)
                        print("Setting time attribute: {}".format(type(datetime_obj)))
                        setattr(self, key, datetime_obj)
                    elif key == "updated_at":
                        datetime_obj = datetime.strptime(value, date_time_format)
                        setattr(self, key, datetime_obj)
                    else: 
                        print("Setting Attribute: key {} value {} of type {}".format(key, value, type(value)))
                        setattr(self, key, value)
        else:
           print("Entring Else statement")
           self.id = uuid4()        
           self.created_at = datetime.now()
           self.updated_at = datetime.now()
           storage.new(self)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Function that updates the public instance attribute `updated at` with the current date and time
        """
        # TODO: Check where storage.save() should come
        self.updated_at = datetime.now()
        storage.save()

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
        return(final_dict)
