import socket 
import threading 
from functools import partial



class Listener(object):
    blacklist_active : bool = True 
    def __init__(self, 
            callback, 
            threaded = True, 
            silence = False, 
            blacklist = None, 
            create_obj = True,
            blacklist_active = True
        ):
        if not callable(callback):
            raise TypeError("Invalid callable %s" % type(callback))    
        if not silence is False and not callable(silence):
            silence = False
            # raise TypeError("Silence argument must be a callable object")
        
        self._threaded = threaded
        self._thread = None 
        self.blacklist = blacklist
        self.func = callback
        self.listening : bool = False 
        self.blacklist_active = blacklist_active
        self.con = None 
        self.count : int = 0
        if create_obj:
            self._createCon()
        self.silence = silence 
            
   
            
    def _createCon(self):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def _startListen(self, *opt, **kwopt):
        self.con.listen(*opt, **kwopt)
        while self.listening:
            try:
                con, addr = self.con.accept()
                if self.blacklist_active:
                    if self.blacklist.has(addr):
                        con.close()
                        continue
    
                self.func(con, addr)
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