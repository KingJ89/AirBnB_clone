#!/usr/bin/python3
"""Module for the Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialization of Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""

