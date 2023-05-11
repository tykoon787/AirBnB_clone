#!/usr/bin/python3
"""
This module define a `Place` class
"""
import models.base_model as bm


class Place(bm.BaseModel):
    """
    class representing a Place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
