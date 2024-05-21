#this is the main the main test file for the console project By Jan Yaya Mutewera

#!/usr/bin/env python3
""" Test Console for AirBnB """
import cmd
import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
import unittest
from models import storage
from models.base_model import BaseModel
import json


class TestConsole(unittest.TestCase):
    """Test the HBNBCommand console."""

    def setUp(self):
        """Set up the test environment."""
        self.console = HBNBCommand()

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("quit")
            self.assertEqual(fake_out.getvalue(), "")

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("EOF")
            self.assertEqual(fake_out.getvalue(), "\n")

    def test_emptyline(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("")
            self.assertEqual(fake_out.getvalue(), "")

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) > 0)
            self.assertIn("BaseModel." + output, storage.all().keys())

    def test_show(self):
        """Test the show command."""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"show BaseModel {model.id}")
            self.assertIn(model.id, fake_out.getvalue())

    def test_destroy(self):
        """Test the destroy command."""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"destroy BaseModel {model.id}")
            self.assertNotIn(f"BaseModel.{model.id}", storage.all())

    def test_all(self):
        """Test the all command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all")
            self.assertTrue(len(fake_out.getvalue()) > 0)

    def test_update(self):
        """Test the update command."""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"update BaseModel {model.id} name 'New Name'")
            self.console.onecmd(f"show BaseModel {model.id}")
            self.assertIn("New Name", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
