#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import city
from models.amenity import Amenity
from models.review import Review
from models import storage
import re
import json

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        return True

    def do_quit(self, arg):
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create a new instance :
usage: create <class name>\n"""
        classes = {"BaseModel": BaseModel, "User": User, "Place": Place, "State": State, "City": City, "Amenity": Amenity, "Review": Review}
        if self._valid(arg):
            args = arg.split()
            if args[0] in classes:
                new_instance = classes[args[0]]()
                storage.save()
                print(new_instance.id)

    def do_clear(self, arg):
        """clear data storage :
usage: clear\n"""
        storage.all().clear()
        self.do_all(arg)
        print("**All data has been cleared! **")

    def _valid(self,arg):
        """Validation of argument passed to commands"""
        args = arg.split()
        _len = len(args)
        if _len == 0:
            print("**class name missing **")
            return False
        if args[0] not in BaseModel.__subclasses__():
            print("**class doesn't exist **")
            return False
        return True

    def _exec(self, arg):
        """parsing, filtering and replacing function"""
        methods = {
            "all": self.do_all,
            "count": self.count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "create": self.do_create
            }


        match = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        args = match[0][0]+" "+match[0][2]
        _list = args.split(", ")
        _list[0] = _list[0].replace('"', "").replace("'", "")
        if len(_list) > 1:
    _list[1] = _list[1].replace('"', "").replace("'", "")
        args = " ".join(_list)
        if match[0][1] in methods:
            methods[match[0][1]](args)

    def default(self, arg):
                        match = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        if len(match) != 0 and match[0][1] == "update" and "{" in arg:
                    _dict = re.search(r'{([^}]+)}', arg).group()
                    _dict = json.loads(_dict.replace("'", '"'))
                    for k, v in _dict.items():
                    _arg = arg.split("{")[0]+k+", "+str(v)+")"
                       self._exec(_arg)
                       elif len(match) != 0:
                       self._exec(arg)


    def do_show(self, arg):
        if self._valid(arg):
            args = arg.split()
            _key = args[0]+"."+args[1]
            print(storage.all()[_key])

    def do_destroy(self, arg):
        if self._valid(arg):
            args = arg.split()
            _key = args[0]+"."+args[1]
            del storage.all()[_key]
            storage.save()

    def do_all(self, arg):
        args = arg.split()
        _len = len(args)
        my_list = []
        if _len >= 1:
            if args[0] not in BaseModel.__subclasses__():
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if args[0] in key:
                    my_list.append(str(value))
        else:
            for key, value in storage.all().items():
                my_list.append(str(value))
        print(my_list)

    def count(self, arg):
        count = 0
        for key in storage.all():
            if arg[:-1] in key:
                count += 1
        print(count)

__name__ == "__main__":
    HBNBCommand().cmdloop()
