#!/usr/bin/env python3

import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it (to the JSON file), and print its id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            obj_id = args[1]
            objs = storage.all()
            key = "{}.{}".format(cls_name, obj_id)
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            obj_id = args[1]
            objs = storage.all()
            key = "{}.{}".format(cls_name, obj_id)
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            all_instances = storage.all(cls_name)
            print([str(instance) for instance in all_instances.values()])
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            obj_id = args[1]
            attr_name = args[2]
            attr_value = args[3]
            objs = storage.all()
            key = "{}.{}".format(cls_name, obj_id)
            if key not in objs:
                print("** no instance found **")
                return
            obj = objs[key]
            setattr(obj, attr_name, attr_value)
            obj.save()
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
