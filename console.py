#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage
import re
import json

# console.py

import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = f"BaseModel.{instance_id}"
        instance = models.storage.get(instance_key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = f"BaseModel.{instance_id}"
        if instance_key in models.storage.all():
            models.storage.delete(instance_key)
            print("** instance deleted **")
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Show all instances based on the class name."""
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
            return
        instances = models.storage.all()
        for instance in instances.values():
            print(instance)

    def do_update(self, arg):
        """Update an instance based on the class name and id by adding or updating an attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]
        instance_key = f"BaseModel.{instance_id}"
        instance = models.storage.get(instance_key)
        if instance:
            setattr(instance, attribute_name, attribute_value)
            instance.save()
            print("** instance updated **")
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

