from typing import List, Dict, Union, Any



    
class ArgumentParser(object):
    _starters = ('-',)
    def __init__(self, data : List[str], required : Dict[str, Any] = dict()):
        self.data : List[str] = data
        self.parsed : Dict[str, str] = {}
        self.required = required
        
    def __enter__(self):
        return self 

    def __exit__(self, exc_type, exc_value, exc_traceback):
        del self.data
        del self.parsed 
        
    def _toBoolean(self, value : str ) -> Union[bool, None]:
        """
        Converts a value to boolean.
        Examples:
            >>> val = _toBoolean('true')
            >>> True
        Args:
            value (int) : The string which will be attempted to convert to boolean.
        Returns:
            bool:  Returns a boolean if the convertion succeeded.
            NoneType: Returns None if the convertion failed
        """
        d = {
            True: ['true', '1', 'enable'],
            False: ['false', '0', 'disable']
        }
        for k, v in d.items():
            if value in v:
                return k
        return None
        
    def parse(self) -> dict:
        cls = self.__class__
        _size = len(self.data)
        for i, value in enumerate(self.data):
            if not value or not any(value.startswith(s) for s in cls._starters):
                continue 
            if (i + 1) < _size:
                _val = self.data[i+1]
                res = self._toBoolean(_val.lower())
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