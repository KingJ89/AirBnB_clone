#!/usr/bin/python3
"""Console module for AirBnB"""
import cmd
import re
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class JHBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB"""
    prompt = "(jhbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    attr_types = {
        "number_rooms": int,
        "number_bathrooms": int,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "longitude": float,
        "name": str,
        "description": str,
        "text": str,
        "email": str,
        "password": str,
        "first_name": str,
        "last_name": str
    }

    def do_EOF(self, arg):
        """Exit the program with EOF command"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in JHBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = JHBNBCommand.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) < 2:
            print("** class name or instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in JHBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instance_key = f"{class_name}.{instance_id}"
        instance = storage.get(instance_key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 2:
            print("** class name or instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in JHBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instance_key = f"{class_name}.{instance_id}"
        if storage.get(instance_key):
            storage.delete(instance_key)
            storage.save()
            print("** instance deleted **")
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        args = arg.split()
        if args and args[0] not in JHBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for instance in storage.all().values():
            if not args or args[0] == instance.__class__.__name__:
                print(instance)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating an attribute"""
        args = re.split(r'\s+', arg, maxsplit=3)
        if len(args) < 4:
            print("** class name, id, attribute name or value missing **")
            return
        class_name, instance_id, attr_name, attr_value = args
        if class_name not in JHBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instance_key = f"{class_name}.{instance_id}"
        instance = storage.get(instance_key)
        if not instance:
            print("** no instance found **")
            return
        if attr_name in JHBNBCommand.attr_types:
            attr_value = JHBNBCommand.attr_types[attr_name](attr_value)
        else:
            attr_value = self.cast_value(attr_value)
        setattr(instance, attr_name, attr_value)
        instance.save()
        print("** instance updated **")

    def cast_value(self, value):
        """Cast value to int or float if possible"""
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            return value

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        if not arg or arg not in JHBNBCommand.classes:
            print("** class name missing or doesn't exist **")
            return
        count = sum(1 for instance in storage.all().values() if instance.__class__.__name__ == arg)
        print(count)

    def default(self, line):
        """Default method for unsupported commands"""
        match = re.match(r'^(\w+)\.(\w+)\((.*)\)$', line)
        if match:
            class_name, method_name, args = match.groups()
            if method_name == "all":
                self.do_all(class_name)
            elif method_name == "count":
                self.do_count(class_name)
            elif method_name == "show":
                self.do_show(f"{class_name} {args}")
            elif method_name == "destroy":
                self.do_destroy(f"{class_name} {args}")
            elif method_name == "update":
                match_args = re.match(r'^"([^"]+)"\s*,\s*({.*})$', args)
                if match_args:
                    instance_id, dict_str = match_args.groups()
                    attr_dict = json.loads(dict_str)
                    for attr, val in attr_dict.items():
                        self.do_update(f"{class_name} {instance_id} {attr} {val}")
                else:
                    self.do_update(f"{class_name} {args}")
            else:
                print(f"** unknown method: {method_name} **")
        else:
            print(f"** unknown syntax: {line} **")


if __name__ == "__main__":
    JHBNBCommand().cmdloop()

