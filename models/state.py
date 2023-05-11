#!/usr/bin/python3
"""
This module defines a `State` class that
inherites from a superclass `BaseClass`
"""
import models.base_model as bm


class State(bm.BaseModel):
    """
    represents a geographical state
    """
    name = ""
