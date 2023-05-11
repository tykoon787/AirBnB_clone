#!/usr/bin/python3
"""
This module defines a user class that inherits from
a superclass BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    represents a user class that inherits from BaseModel
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
