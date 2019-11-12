#!/usr/bin/python3
"""
This is the entry point to the HBnB console
"""
import cmd
import re
import json
import uuid
from models import storage


class CMDParser:
    """
    Parser class for AirBnB console
    """
    __composite_regex = re.compile(r"^(\w+).(\w+)\((.+)|\B\)$")
    __simple_regex = re.compile(r"^(\w+) (.+)$")

    def __init__(self, line):
        self.classname = ''
        self.operation = ''
        self.uuid = ''
        self.params = ''

        match_composite = CMDParser.__composite_regex.fullmatch(line)
        match_simple = CMDParser.__simple_regex.fullmatch(line)

        if match_composite:
            self.assign_composite(match_composite)
        elif match_simple:
            self.assign_simple(match_simple)
        else:
            self.operation = line

    def assign_composite(self, match):
        """
        Assigns a composite regex
        """
        self.classname = match.group(1)
        self.operation = match.group(2)

        if match.group(3):
            par_list = match.group(3).split(',', 1)
            if len(par_list) >= 1:
                self.uuid = par_list[0]
                self.uuid = self.uuid.replace('\"', '')
            if len(par_list) >= 2:
                word = par_list[1].strip().replace(')', '')
                dict_regex = re.compile(r"^\{.+\}$")
                dict_match = dict_regex.fullmatch(word)
                if dict_match:
                    self.params = word\
                        .replace("\'", '\"')\
                        .replace('{', '')\
                        .replace('}', '')
                else:
                    self.params = word.replace(',', ':')

    def assign_simple(self, match):
        """
        Assigns a simple regex
        """
        self.operation = match.group(1)

        if match.group(2):
            par_list = match.group(2).split(' ', 2)

            self.classname = par_list[0] if len(par_list) >= 1 else ''
            self.uuid = par_list[1] if len(par_list) >= 2 else ''

            if self.uuid:
                self.uuid = self.uuid.replace('\"', '')

            if len(par_list) >= 3:
                skell = par_list[2]\
                    .replace('\"', '')\
                    .replace("\'", '')\
                    .split(' ', 1)
                if len(skell) >= 2:
                    self.params = '\"{}\": \"{}\"'.format(*skell)
                else:
                    err_k = hex(uuid.getnode())
                    self.params = '\"{}\": \"{}\"'.format(err_k, 'NO_VAL')


class HBNBCommand(cmd.Cmd):
    """
    AirBnB console main class
    """
    __pc_id = hex(uuid.getnode())
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
             'ID_NOEX': "** no instance found **",
             'NO_ATTR': "** attribute name missing **",
             'NO_VAL': "** value missing **"}

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

    def do_update(self, jsargs):
        """
        update - Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        argdict = self.reparse(jsargs)

        checks = (argdict is None,
                  not argdict,
                  'classname' not in argdict.keys())
        if any(checks):
            print(HBNBCommand.__err['CLS_MISS'])
            return

        class_name = argdict['classname']

        if not self.is_valid_class(class_name):
            print(HBNBCommand.__err['CLS_NOEX'])
            return

        if 'id' not in argdict.keys():
            print(HBNBCommand.__err['ID_MISS'])
            return

        obj_id = argdict['id']
        key_name = class_name + "." + obj_id

        if key_name not in storage._FileStorage__objects:
            print(HBNBCommand.__err['ID_NOEX'])
            return

        if len(argdict) <= 2:
            print(HBNBCommand.__err['NO_ATTR'])
            return

        if HBNBCommand.__pc_id in argdict:
            print(HBNBCommand.__err[argdict[HBNBCommand.__pc_id]])
            return

        storage._FileStorage__objects.pop(key_name)
        storage.save()
        storage.reload()
        mod_name = HBNBCommand.__avail_cls[class_name]
        instance = self.spawn('models', mod_name, class_name)
        temp_key = "{}.{}".format(class_name, instance.id)
        storage._FileStorage__objects.pop(temp_key)
        for k, v in argdict.items():
            if k == 'classname':
                pass
            else:
                setattr(instance, k, v)
        storage.new(instance)
        instance.save()

    def do_count(self, jsargs):
        """
        Count the total objects of a given class
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
