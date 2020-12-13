from typing import List

from packet.lib.clients import Client


class Connections(object):
    def __init__(self):
        self.connections : List[Client] = []
        
    def __call__(self):
        return self.connections
    
    def add(self, con):
        self.connections.append(con)