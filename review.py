#!/usr/bin/python3
"""
This module defines a `Review` class that
inherits from a superclass `BaseModel`
"""
import models.base_model as bm 


class Review(bm.BaseModel):
    """
    class representation of a Review
    """
    place_id = ""
    user_id = ""
    text = ""
