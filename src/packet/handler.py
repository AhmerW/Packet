from packet.common.singleton import Singleton

class EventHandler(object, metaclass = Singleton):
    def __init__(self, cli = False):
        self._cli = cli
        
    def start(self):
        pass