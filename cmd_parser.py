import re


class CMDParser:
    """
    Parser class for AirBnB console
    """
    __composite_regex = re.compile(r"^(\w+).(\w+)\(([^\{\}]+|\B)\)$")
    __dict_regex = re.compile(r"^(\w+).(\w+)\((.+)\)$")
    __simple_regex = re.compile(r"^(\w+) (\w+|\B) (.+|\B)$")
    __duo_regex = re.compile(r"^(\w+) (\w+|\B)$")

    def __init__(self, line):
        self.classname = ''
        self.operation = ''
        self.params = ''

        match_composite = CMDParser.__composite_regex.fullmatch(line)
        match_dict = CMDParser.__dict_regex.fullmatch(line)
        match_simple = CMDParser.__simple_regex.fullmatch(line)
        match_duo = CMDParser.__duo_regex.fullmatch(line)

        if match_composite:
            self.assign_composite(match_composite)
        elif match_dict:
            self.assign_composite(match_dict)
        elif match_simple:
            self.assign_simple(match_simple)
        elif match_duo:
            self.operation = match_duo.group(1)
            self.classname = match_duo.group(2)
        else:
            self.operation = line

    def assign_composite(self, match):
        """
        Assigns a composite regex
        """
        self.classname = match.group(1)
        self.operation = match.group(2)
        self.params = match.group(3)
        if self.params:
            self.trim()

    def assign_simple(self, match):
        """
        Assigns a simple regex
        """
        self.operation = match.group(1)
        self.classname = match.group(2) if match.group(2) else ''
        self.params = match.group(3) if match.group(3) else ''
        if self.params:
            self.trim()

    def trim(self):
        """
        Trims unwanted characters
        """
        removes = [34, 39, 44, 58, 123, 125]
        if self.params is None or not self.params:
            pass
        else:
            for c in removes:
                self.params = self.params.translate({c: None})
