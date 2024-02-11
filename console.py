#!/usr/bin/python3
"""
Console module for AirBnB clone command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the console using EOF (Ctrl+D)
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
