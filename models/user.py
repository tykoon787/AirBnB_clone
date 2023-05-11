#!/usr/bin/python3
"""
This module defines a user class

"""
import models.base_model as bm

class User(bm.BaseModel):
    """
    This is the user class
    ...
    Attributes
    ----------
    email: str
        Email of the User
    password: str
        User Password
    first_name: str
        User First Name
    last_name: str
        User Last Name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    