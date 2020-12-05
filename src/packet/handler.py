
from packet.common.singleton import Singleton
from packet.ui.window import PacketWindow
from packet.lib.network import Listener
from PyQt5 import QtWidgets, QtCore

from typing import List 

class EventHandler(object, metaclass = Singleton):
    def __init__(self, cli = False):
        self._cli = cli
        self.app : QtWidgets.QApplication = None
        self.window : PacketWindow = None
        self.listeners : List[Listener] = list()
        
    def loadWindow(self):
        self.app = QtWidgets.QApplication([])
        self.window = PacketWindow()
        self.window.show()
        self.app.exec_()
    
    def loadCli(self):
        pass
    
    def start(self):
        
        if not self._cli:
            self.loadWindow()
        else:
            self.loadCli()
            
        return self 