import socket 
import threading 
from functools import partial

class Listener(object):
    create_socket = True 
    def __init__(self, callback, threaded = True, silence = False ):
        if not callable(callback):
            raise TypeError("Invalid callable %s" % type(callback))
        self._threaded = threaded
        self._thread = None 
        self.func = callback
        self.listening : bool = False 
        self.con = None 
        self.count : int = 0
        if self.__class__.create_socket:
            self._createCon()
            
        if not silence is False and not callable(silence):
            raise TypeError("Silence argument must be a callable object")
        self.silence = silence 
            
    @property
    def threaded(self):
        return self._threaded 
    
    @threaded.setter
    def threadedSetter(self, value : bool):
        if not isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Invalid value for theaded attribute %s" % type(value))
        
        self._threaded = bool(threaded) if hasattr(threaded, '__bool__') else threaded
            
    def _createCon(self):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def _startListen(self, *opt, **kwopt):
        self.con.listen(*opt, **kwopt)
        while self.listening:
            try:
                self.func(*self.con.accept())
                self.count += 1
            except Exception as e:
                if not self.silence is False:
                    self.silence(e)
                else: raise e
            
    def listen(self, *a, **kw) -> bool:
        if not self.con:
            self._createCon()
        if self.listening:
            return False
        self.listening = not self.listening
        if self._threaded:
            self._thread = threading.Thread(
                partial(self._startListen, *a, **kw)
            )
            self._thread.start()
        else:
            self._startListen(*a, **kw)