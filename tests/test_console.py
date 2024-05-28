#this is the main the main test file for the console project By Jan Yaya Mutewera

#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import JHBNBCommand
from models import storage
from models.base_model import BaseModel
import re


class TestJHBNBCommand(unittest.TestCase):
    """Test the JHBNBCommand console."""

    def setUp(self):
        """Set up the test environment."""
        self.console = JHBNBCommand()
        storage.all().clear()

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
            self.assertIn(f"BaseModel.{output}", storage.all().keys())

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
            self.assertNotIn(f"BaseModel.{model.id}", storage.all().keys())

    def test_all(self):
        """Test the all command."""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all")
            self.assertIn(model.id, fake_out.getvalue())

    def test_update(self):
        """Test the update command."""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'update BaseModel {model.id} name "New Name"')
            self.assertIn("New Name", fake_out.getvalue())
            updated_model = storage.get(f"BaseModel.{model.id}")
            self.assertEqual(updated_model.name, "New Name")

    def test_count(self):
        """Test the count command."""
        model1 = BaseModel()
        model2 = BaseModel()
        model1.save()
        model2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("count BaseModel")
            self.assertEqual(fake_out.getvalue().strip(), "2")

    def test_default_all(self):
        """Test the default all method."""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("BaseModel.all()")
            self.assertIn(model.id, fake_out.getvalue())

    def test_default_show(self):
        """Test the default show method."""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"BaseModel.show({model.id})")
            self.assertIn(model.id, fake_out.getvalue())

    def test_default_destroy(self):
        """Test the default destroy method."""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"BaseModel.destroy({model.id})")
            self.assertNotIn(f"BaseModel.{model.id}", storage.all().keys())

    def test_default_update(self):
        """Test the default update method."""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'BaseModel.update({model.id}, "name", "New Name")')
            self.assertIn("New Name", fake_out.getvalue())
            updated_model = storage.get(f"BaseModel.{model.id}")
            self.assertEqual(updated_model.name, "New Name")

    def test_default_update_with_dict(self):
        """Test the default update method with dictionary."""
        model = BaseModel()
        model.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'BaseModel.update({model.id}, {{"name": "New Name", "age": 30}})')
            self.assertIn("New Name", fake_out.getvalue())
            updated_model = storage.get(f"BaseModel.{model.id}")
            self.assertEqual(updated_model.name, "New Name")
            self.assertEqual(updated_model.age, 30)


if __name__ == '__main__':
    unittest.main()

