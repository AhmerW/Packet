import socket 
import time 

from typing import List

from packet.lib.network import Listener


class Client(object):
    def __init__(self):
        self.con : socket.socket = None
    
        
        
class User(object):
    def __init__(self):
        
        # information 
        self.created = time.time()
        
        # objects 
        self.listeners : List[Listener] = list()
        
    