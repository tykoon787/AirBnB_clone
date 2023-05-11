#!/usr/bin/python3
"""
This module defines a `State` class that
inherites from a superclass `BaseClass`
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    represents a geographical state
    """
    name = ""
