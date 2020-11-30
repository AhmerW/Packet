
from typing import Union, Any

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