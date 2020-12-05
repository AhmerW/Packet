from typing import List, Union

from packet.common.argparse import ArgumentParser
from packet.handler import EventHandler

class Packet(object):
    """ 
    Main Packet class. Holds all objects and is the 
    'linker'.
    """
    default_args = {
        'cli': False
    }
    
    def __init__(self):
        self._cli = False
        self.handler : Union[None, EventHandler] = None
    
    
    def load(self, args : List[str]):
        with ArgumentParser(args, required = self.__class__.default_args) as parser:
            args = parser.parse()
        print(args)
        self._cli = bool(args.get('cli'))
        self.handler = EventHandler(self._cli).start()
        