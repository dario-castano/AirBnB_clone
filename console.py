#!/usr/bin/python3
"""
This is the entry point to the HBnB console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    AirBnB console main class
    """
    __avail_cls = {'BaseModel': 'base_model',
                   'Amenity': 'amenity',
                   'City': 'city',
                   'Place': 'place',
                   'Review': 'review',
                   'State': 'state',
                   'User': 'user'}

    __err = {'CLS_MISS': "** class name missing **",
             'CLS_NOEX': "** class doesn't exist **",
             'ID_MISS': "** instance id missing **",
             'ID_NOEX': "** no instance found **"}

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
        if argstr is None or not argstr:
            print(HBNBCommand.__err['CLS_MISS'])
            return
        arglist = self.parse(argstr)
        class_name = arglist[0]
        if class_name in HBNBCommand.__avail_cls:
            mod_name = HBNBCommand.__avail_cls[class_name]
            instance = self.spawn('models', mod_name, class_name)
            instance.save()
            print(instance.id)
        else:
            print(HBNBCommand.__err['CLS_NOEX'])

    def do_show(self, argstr):
        """
        show - Prints the string representation of an instance
        based on the class name and id
        """
        arglist = self.parse(argstr)

    def do_destroy(self, argstr):
        """
        destroy - Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        arglist = self.parse(argstr)

    def do_all(self, argstr):
        """
        all - Prints all string representation of all instances
        based or not on the class name
        """
        arglist = self.parse(argstr)

    def do_update(self, argstr):
        """
        update - Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        arglist = self.parse(argstr)

    def parse(self, line):
        """
        Parse string to a string tuple
        """
        return tuple(line.split())

    def is_valid_class(self, str_cls):
        """
        Checks if is a valid class
        """
        if str_cls in HBNBCommand.__avail_cls:
            return True
        else:
            return False

    def spawn(self, pack, module, clsname):
        """
        Spawns an instance of a given class
        """
        imp = __import__(pack)
        md = getattr(imp, module)
        cls = getattr(md, clsname)
        return cls()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

