
class Singleton(type):
    _cls = None 
    def __new__(cls, name, base, attrs):
        if not cls._cls:
            cls._cls = type(name, base, attrs)
        return cls._cls
            