#!/usr/bin/python3
"""This module contains the console for AirBnB"""
import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """This class contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

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
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        new = BaseModel()
        new.save()
        print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234"""
        if not arg:
            print("** class name missing **")
            return
        if arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(arg.split()) < 2:
            print("** instance id missing **")
            return
        key = arg.split()[0] + "." + arg.split()[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234"""
        if not arg:
            print("** class name missing **")
            return
        if arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(arg.split()) < 2:
            print("** instance id missing **")
            return
        key = arg.split()[0] + "." + arg.split()[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        models.storage.all().pop(key)
        models.storage.save()
    
    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the
        class name. Ex: $ all BaseModel or $ all"""
        if not arg:
            print([str(v) for v in models.storage.all().values()])
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        print([str(v) for k, v in models.storage.all().items() if k.split(".")[0] == arg])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). Ex: $ update
        BaseModel 1234-1234-1234 email """
        if not arg:
            print("** class name missing **")
            return
        if arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(arg.split()) < 2:
            print("** instance id missing **")
            return
        key = arg.split()[0] + "." + arg.split()[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(arg.split()) < 3:
            print("** attribute name missing **")
            return
        if len(arg.split()) < 4:
            print("** value missing **")
            return
        setattr(models.storage.all()[key], arg.split()[2], arg.split()[3])
        models.storage.all()[key].save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()