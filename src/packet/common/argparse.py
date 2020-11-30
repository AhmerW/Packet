from typing import List, Dict, Union, Any

from packet.common.converters import toBoolean

    
class ArgumentParser(object):
    starters = ('-',)
    
    def __init__(self, data : List[str], required : Dict[str, Any] = dict()):
        self.data : List[str] = data
        self.parsed : Dict[str, str] = {}
        self.required = required
        
    def __enter__(self):
        return self 

    def __exit__(self, exc_type, exc_value, exc_traceback):
        del self.data
        del self.parsed 
        
        
    def parse(self) -> dict:
        cls = self.__class__
        _size = len(self.data)
        for i, value in enumerate(self.data):
            if not value or not any(value.startswith(s) for s in cls.starters):
                continue 
            if (i + 1) < _size:
                _val = self.data[i+1]
                res = toBoolean(_val.lower())
                if not res is None:
                    _val = res
                self.parsed[value.replace(value[0], '')] = _val
                
        if self.required:
            for k, v in self.required.items():
                s = self.parsed.get(k)
                if isinstance(s, type(v)):
                    continue
                self.parsed[k] = v
            
        return self.parsed