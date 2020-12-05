
from typing import Union, Any
from re import match

def toBoolean(value, l1 = None, l2 = None, default = None) -> Any:
    if not l1 or l2:
        l1, l2 = ['true', '1', 'enable'], ['false', '0', 'disable']
    if default is False:
        return value in l1 
    if value in l1:
        return True 
    elif value in l2:
        return False 
    return default

def toInt(value, default = None ):
    if bool(match(r"^[0-9]+$", value)):
        try:
            return int(value)
        except ValueError:
            return default
    return default