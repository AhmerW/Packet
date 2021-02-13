import re 

class Regex:
    integer_only = r"^[-+]?[0-9]+$"
    letters_only = r"^[A-Za-z]+$"

    
    @classmethod
    def match(cls, regex, data):
        return bool(re.match(regex, data))
    
    @classmethod 
    def craftContainer(cls, regex, containers = [], index = 0):
        _rgx = regex.split("]")
        _rgx[index] = _rgx[index]+"".join(containers)+"]"
        return r''.join(_rgx)


def validateEntries(entries):
    return {
        entry : Regex.match(regex, entry.text().strip()) for entry, regex 
        in entries.items() if not regex is None
    }
    
