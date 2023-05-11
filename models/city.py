#!/usr/bin/python3
"""
This module defines a `City` class
that inherits from a superclass `BaseModel`
"""
import models.base_model as bm


class City(bm.BaseModel):
    """
    class representation of a city
    """
    state_id = ""
    name = ""
