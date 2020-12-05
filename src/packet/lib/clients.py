import socket 

class Client(object):
    def __init__(self):
        self.con : socket.socket = None
        
        
class User(object):
    def __init__(self):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    