#!/usr/bin/python3
"""
This is the entry point to the HBnB console
"""
import cmd
import json
from cmd_parser import CMDParser
from models import storage


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

    def parseline(self, line):
        answer = CMDParser(line)

        new_line = '{'
        if answer.classname:
            new_line += '"classname": "{}"'.format(answer.classname)
        if answer.uuid:
            new_line += ', "id": "{}"'.format(answer.uuid)
        if answer.params:
            new_line += ', ' + answer.params
        new_line += '}'

        if new_line == '{}':
            return answer.operation, '', line
        elif answer.operation == 'help':
            return answer.operation, answer.classname, line
        else:
            return answer.operation, new_line, line

    def do_EOF(self, jsargs):
        """
        EOF - Exits if EOF is detected
        """
        return True

    def do_quit(self, jsargs):
        """
        quit - Exits the console
        """
        return True

    def do_create(self, jsargs):
        """
        create - Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        argdict = self.reparse(jsargs)

        checks = (argdict is None,
                  not argdict,
                  'classname' not in argdict.keys())
        if any(checks):
            print(HBNBCommand.__err['CLS_MISS'])
            return

        class_name = argdict['classname']

        if self.is_valid_class(class_name):
            mod_name = HBNBCommand.__avail_cls[class_name]
            instance = self.spawn('models', mod_name, class_name)
            instance.save()
            print(instance.id)
        else:
            print(HBNBCommand.__err['CLS_NOEX'])

    def do_show(self, jsargs):
        """
        show - Prints the string representation of an instance
        based on the class name and id
        """
        argdict = self.reparse(jsargs)

        checks = (argdict is None,
                  not argdict,
                  'classname' not in argdict.keys(),
                  not argdict['classname'])
        if any(checks):
            print(HBNBCommand.__err['CLS_MISS'])
            return

        class_name = argdict['classname']

        if self.is_valid_class(class_name) is False:
            print(HBNBCommand.__err['CLS_NOEX'])
            return

        if 'id' not in argdict.keys():
            print(HBNBCommand.__err['ID_MISS'])
            return

        obj_id = argdict['id']
        key_name = class_name + "." + obj_id

        if key_name in storage._FileStorage__objects:
            print(storage._FileStorage__objects[key_name])
        else:
            print(HBNBCommand.__err['ID_NOEX'])

    def do_destroy(self, jsargs):
        """
        destroy - Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        argdict = self.reparse(jsargs)

        checks = (argdict is None,
                  not argdict,
                  'classname' not in argdict.keys())
        if any(checks):
            print(HBNBCommand.__err['CLS_MISS'])
            return

        class_name = argdict['classname']

        if self.is_valid_class(class_name) is False:
            print(HBNBCommand.__err['CLS_NOEX'])
            return

        if 'id' not in argdict.keys():
            print(HBNBCommand.__err['ID_MISS'])
            return

        obj_id = argdict['id']
        key_name = class_name + "." + obj_id

        if key_name in storage._FileStorage__objects:
            del storage._FileStorage__objects[key_name]
            storage.save()
        else:
            print(HBNBCommand.__err['ID_NOEX'])

    def do_all(self, jsargs):
        """
        all - Prints all string representation of all instances
        based or not on the class name
        """
        argdict = self.reparse(jsargs)

        checks = (argdict is None,
                  not argdict,
                  'classname' not in argdict.keys())
        if any(checks):
            obj_list = []
            for key in storage._FileStorage__objects:
                obj_list.append(str(storage._FileStorage__objects[key]))
            print(obj_list)
            return

        class_name = argdict['classname']

        if self.is_valid_class(class_name):
            obj_list = []
            for key in storage._FileStorage__objects:
                if class_name in key:
                    obj_list.append(str(storage._FileStorage__objects[key]))
            print(obj_list)
        else:
            print(HBNBCommand.__err['CLS_NOEX'])

    def do_update(self, argstr):
        """
        update - Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        arglist = self.reparse(argstr)

    def do_count(self, jsargs):
        """
        Count the total objects of a given class
        """
        argdict = self.reparse(jsargs)

        checks = (argdict is None,
                  not argdict,
                  'classname' not in argdict.keys(),
                  not argdict['classname'])
        if any(checks):
            print(HBNBCommand.__err['CLS_MISS'])
            return

        class_name = argdict['classname']

        if self.is_valid_class(class_name):
            obj_count = 0
            for keys in storage._FileStorage__objects.keys():
                if class_name in keys:
                    obj_count += 1
            print(obj_count)
        else:
            print(HBNBCommand.__err['CLS_NOEX'])

    def reparse(self, line):
        """
        Parse JSON - string to a string dictionary
        """
        if line:
            return json.loads(line)
        else:
            return dict()

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
