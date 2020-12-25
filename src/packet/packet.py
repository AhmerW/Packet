from typing import List, Union, Dict

from packet.common.argparse import ArgumentParser
from packet.handler import EventHandler
from packet.lib.clients import User

default_args = {
    'cli': False
}

class Packet(object):
    """ 
    Main Packet class. 
    """
    def __init__(self):
        self.handler : EventHandler = None
        self.user = User()
    
    
    def load(self, args : List[str]):
        with ArgumentParser(args, required = default_args) as parser:
            args = parser.parse()
        self.cli = bool(args.get('cli'))
        self.handler = EventHandler(self).start()
        