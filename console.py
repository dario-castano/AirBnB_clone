#!/usr/bin/python3
"""
This is the entry point to the HBnB console
"""
import cmd
import signal


class HBNBCommand(cmd.Cmd):
    """
    AirBnB console main class
    """
    def __init__(self):
        super().__init__()
        self.prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """
        EOF - Exits if EOF is detected
        """
        return True

    def do_quit(self, *args):
        """
        quit - Exits the console
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

