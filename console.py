#!/usr/bin/python3
"""Module for console command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            with open("file.json", 'r') as f:
                objects = json.load(f)
        except FileNotFoundError:
            print("** no instance found **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        try:
            with open("file.json", 'r') as f:
                objects = json.load(f)
        except FileNotFoundError:
            print("** no instance found **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]

        with open("file.json", 'w') as f:
            json.dump(objects, f)

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        if not arg:
            objects = FileStorage().all()
            objects = [str(obj)
                       for obj in objects.values()
                       if isinstance(obj, BaseModel)]
            print(instances)
            return

        args = arg.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        objects = FileStorage().all()
        instances = [
                str(obj) for k, obj in objects.items()
                if args[0] in k and isinstance(obj, BaseModel)
                ]
        print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = self.reload_objects()
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        setattr(objects[key], args[2], args[3])
        objects[key].save()

    def do_quit(self, arg):
        """
        Quit command to exit program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program
        """
        print()
        return True

    def emptyline(self):
        pass

    def reload_objects(self):
        """
        Deserializes the JSON file and reloads objects into the dictionary
        """
        objects = {}
        try:
            with open("file.json", 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    objects[key] = BaseModel.from_dict(value)
        except FileNotFoundError:
            pass
        return objects


if __name__ == '__main__':
    HBNBCommand().cmdloop()
