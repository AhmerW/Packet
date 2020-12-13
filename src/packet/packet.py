from typing import List, Union, Dict

from packet.common.argparse import ArgumentParser
from packet.handler import EventHandler

default_args = {
    'cli': False
}

class Packet(object):
    """ 
    Main Packet class. Holds all objects and is the 
    'linker'.
    """
    def __init__(self):
        self.handler : EventHandler = None
    
    
    def load(self, args : List[str]):
        with ArgumentParser(args, required = default_args) as parser:
            args = parser.parse()
        print(args)
        self._cli = bool(args.get('cli'))
        self.handler = EventHandler(self._cli).start()
        