#!/usr/bin/python3
"""
This module implements a command interpreter for the HBNB project.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the HBNB project.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program
        """
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
