#!/usr/bin/python3
"""
This module defines a `Review` class that
inherits from a superclass `BaseModel`
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class representation of a Review
    """
    place_id = ""
    user_id = ""
    text = ""
