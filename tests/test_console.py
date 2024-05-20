import unittest
import json
import os
from console import User, StorageEngine, JSONFilePersistence, Console

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.storage = StorageEngine()
        self.persistence = JSONFilePersistence("test_data.json")
        self.console = Console(self.storage, self.persistence)

    def tearDown(self):
        if os.path.exists("test_data.json"):
            os.remove("test_data.json")

    def test_create_user(self):
        self.console.onecmd("create_user 1 John john@example.com")
        user = self.storage.read(1)
        self.assertIsNotNone(user)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "John")
        self.assertEqual(user.email, "john@example.com")

    def test_create_user_invalid_args(self):
        result = self.console.onecmd("create_user")
        self.assertIn("Invalid arguments", result)

    def test_read_user(self):
        self.storage.create(User(id=1, name="John", email="john@example.com"))
        result = self.console.onecmd("read_user 1")
        self.assertIn("ID: 1, Name: John, Email: john@example.com", result)

    def test_read_user_not_found(self):
        result = self.console.onecmd("read_user 1")
        self.assertIn("User not found", result)

    def test_update_user(self):
        self.storage.create(User(id=1, name="John", email="john@example.com"))
        self.console.onecmd("update_user 1 Jane jane@example.com")
        user = self.storage.read(1)
        self.assertEqual(user.name, "Jane")
        self.assertEqual(user.email, "jane@example.com")

    def test_update_user_not_found(self):
        result = self.console.onecmd("update_user 1 Jane jane@example.com")
        self.assertIn("User not found", result)

    def test_update_user_invalid_args(self):
        result = self.console.onecmd("update_user")
        self.assertIn("Invalid arguments", result)

    def test_delete_user(self):
        self.storage.create(User(id=1, name="John", email="john@example.com"))
        self.console.onecmd("delete_user 1")
        user = self.storage.read(1)
        self.assertIsNone(user)

    def test_delete_user_not_found(self):
        result = self.console.onecmd("delete_user 1")
        self.assertIn("User not found", result)

    def test_delete_user_invalid_args(self):
        result = self.console.onecmd("delete_user")
        self.assertIn("Invalid arguments", result)

if __name__ == "__main__":
    unittest.main()

