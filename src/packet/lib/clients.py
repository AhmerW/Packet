import socket 
import time 

from typing import List

from packet.lib.network import Listener

class NetworkErrors:
    Refused = 1
    Invalid = 2
    


class Connection():
    def __init__(self):
        self.con : socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        
    def connect(self, ip, port):
        return self.con.connect((ip, port))
    
class User(object):
    def __init__(self):
        
        # information 
        self.created = time.time()
        
        # objects 
        self.connections : List[Connection] = list()
        self.listeners : List[Listener] = list()
        
    def createConnection(self, ip = None, port = None, _id = None) -> bool:
        if all(x is None for x in (ip, port, _id)):
            return False 
        if _id is None and (ip is None or port is None):
            return False 
        if _id is None:
            cdata = ip, port 
        else: 
            cdata = ... 
            # get cdata from server 
            return False 
        try:
            con = Connection().connect(*cdata)
            self.connections.append(con)
            return True
        except Exception as e:
            return False 