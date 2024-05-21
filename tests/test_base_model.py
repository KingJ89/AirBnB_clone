#!/usr/bin/bash/env python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def setUp(self):
        """Set up test methods."""
        self.model = BaseModel()

    def test_id(self):
        """Test if id is a string of a valid UUID."""
        self.assertIsInstance(self.model.id, str)
        self.assertTrue(uuid.UUID(self.model.id))

    def test_created_at(self):
        """Test if created_at is a datetime object."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is a datetime object."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test the string representation of the instance."""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        """Test if updated_at is updated on save."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test if to_dict method returns the correct dictionary."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())

    def test_kwargs(self):
        """Test initialization with kwargs."""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)
        self.assertEqual(new_model.to_dict(), self.model.to_dict())


if __name__ == "__main__":
    unittest.main()

