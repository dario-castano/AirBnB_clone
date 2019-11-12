#!/usr/bin/python3
"""
Module that helps to parse lines for the console
"""
import re
import uuid

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


