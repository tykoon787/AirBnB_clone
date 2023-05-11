#!/usr/bin/python3
"""
This module defines a `City` class
that inherits from a superclass `BaseModel`
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class representation of a city
    """
    state_id = ""
    name = ""
