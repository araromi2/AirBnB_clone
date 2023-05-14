#!/usr/bin/python3
"""This module contains the console for the AirBnB project"""
import cmd
import json
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(
                    arg.split()[0],
                    arg.split()[1]
                    )
            objects = models.storage.all()
            if obj_key in objects:
                print(objects[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(
                    arg.split()[0],
                    arg.split()[1]
                    )
            objects = model.storage.all()
            if obj_key in objects:
                del objects[obj_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print the string represnetation of all instances"""
        objects = models.storage.all()
        obj_list = []
        if not arg:
            for obj_key in objects:
                obj_list.append(str(objects[obj_key]))
        elif arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            for obj_key in objects:
                if obj_key.split(".")[0] == arg.split()[0]:
                    obj_list.append(str(objects[obj_key]))
        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        elif len(arg.split()) < 3:
            print("** attribute name missing **")
        elif len(arg.split()) < 4:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(
                    arg.split()[0],
                    arg.split()[1]
                    )
            objects = models.storage.all()
            if obj_key in objects:
                instance = objects[obj_key]
                attribute_name = arg.split()[2]
                attribute_value = arg.split()[3]
                setattr(instance, attribute_name, attribute_value)
                instance.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
