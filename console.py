#!/usr/bin/python3

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Console for AirBnB clone"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg or arg == "":
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
        except:
            print("** class doesn't exist **")
            return
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg or arg == "":
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            all_instances = models.storage.all()
            key = args[0] + "." + args[1]
            print(all_instances[key])
        except:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if not arg or arg == "":
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            all_instances = models.storage.all()
            key = args[0] + "." + args[1]
            del all_instances[key]
            models.storage.save()
        except:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        all_instances = models.storage.all()
        if not arg or arg == "":
            for key, value in all_instances.items():
                print(value)
        else:
            try:
                for key, value in all_instances.items():
                    if arg in key:
                        print(value)
            except:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
        if not arg or arg == "":
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        try:
            all_instances = models.storage.all()
            key = args[0] + "." + args[1]
            setattr(all_instances[key], args[2], args[3])
            models.storage.save()
        except:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()