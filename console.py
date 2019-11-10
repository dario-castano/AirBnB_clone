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

    def do_EOF(self, argstr):
        """
        EOF - Exits if EOF is detected
        """
        return True

    def do_quit(self, argstr):
        """
        quit - Exits the console
        """
        return True

    def do_create(self, argstr):
        """
        create - Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        pass

    def do_show(self, argstr):
        """
        show - Prints the string representation of an instance
        based on the class name and id
        """
        pass

    def do_destroy(self, argstr):
        """
        destroy - Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        pass

    def do_all(self, argstr):
        """
        all - Prints all string representation of all instances
        based or not on the class name
        """
        pass

    def do_update(self, argstr):
        """
        update - Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        pass

    def parse(self, string):
        return tuple(string.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()

