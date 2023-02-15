#!/usr/bin/python3

from models import storage
from models.user import User
from models.base_model import BaseModel

if __name__ == "__main__":

        
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("---- Crete Base Model Clas --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)

    print("-- Create a new User --")
    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Bar"
    my_user.email = "airbnb@mail.com"
    my_user.password = "root"
    my_user.save()
    print(my_user)

    print("-- Create a new User 2 --")
    my_user2 = User()
    my_user2.first_name = "John"
    my_user2.email = "panda@mail.com"
    my_user2.password = "bamboo"
    my_user2.save()
    print(my_user2)
