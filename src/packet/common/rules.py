class Blacklist():
    count : int = 0
    def __init__(self, db = True):
        self._data = []
        self._db = {}
        
        self.db_active = db
        self.maximum = None
        self.active = True 
        self.count = self.__class__.count 
        self.__class__.count += 1
        
    def __str__(self):
        return "<Blacklist Rule [{0}]>".format(self.count)
    
    
    @property
    def data(self):
        return self._data
    
    @property 
    def db(self):
        return self._db
    
    def reset_db(self, value) -> bool:
        if self._db.get(value):
            del self._db[value]
            return True 
        return False
        
    def has(self, value) -> bool:
        return value in self._data
        
    def add(self, value) -> bool:
        if self.maximum:
            if len(self._data) >= self.maximum:
                return False 
        if self.db_active:
            if self._db.get(value):
                self._db[value] += 1
            else:
                self._db[value] = 0
        self._data.append(value)
        return True
    
    def remove(self, value, reset = False ) -> bool:
        try:
            self._data.remove(value)
            if reset and self._db.get(value):
                self.reset_db(value)
            return True
        except:
            return False
        