from PyQt5 import QtWidgets, QtCore
from functools import partial
from typing import List 


from packet.common.singleton import Singleton
from packet.ui.window import PacketWindow
from packet.lib.network import Listener

from packet.ui.dialogs import TestDialog

mapped = {
    "news": 1,
    "create_a_connection": 3
}

class Events(object):
    def __init__(self, window):
        self.window = window

    def itemClicked(self, obj, col):
        text = obj.text(col)
        data = mapped.get(
            text.lower().replace(' ', '_'), 
            0
        )
        func = None
        if isinstance(data, list):
            if len(data) == 1:
                index = data[0]
            elif len(data) == 2:
                index, func = data
            else: return 
        else:
            index = data 
        if not index is None:   
            self.window.mainFrame.setCurrentIndex(index)
        if callable(func):
            func()
        if index == 3:
            print("a")
            obj = TestDialog(self.window)
            obj.show()
            obj.exec_()
      
        
    def buttonClicked(self, button):
        pass

class EventHandler(object, metaclass = Singleton):
    def __init__(self, cli = False):
        self._cli = cli
        self.app : QtWidgets.QApplication = None
        self.window : PacketWindow = None
        self.events : Events = None
        self.listeners : List[Listener] = list()
        
    def loadWindow(self):
        self.app = QtWidgets.QApplication([])
        self.window = PacketWindow()
        self.events = Events(self.window)
        self.window.show()
        
    
    def loadCli(self):
        pass

    def start(self):
        if not self._cli:
            self.loadWindow()
            self._bindButtons()
            self.app.exec_()
        else:
            self.loadCli()
        return self 
    
    def _bindButtons(self):
        if not self.window:
            raise TypeError("Window not initalized")
        for name, obj in self.window.__dict__.items():
            if isinstance(obj, QtWidgets.QPushButton) or isinstance(obj, QtWidgets.QToolButton):
                if not hasattr(obj, 'clicked'):
                    if hasattr(obj, 'triggered'):
                        obj.triggered.connect(partial(self.events.buttonClicked, name))
                    continue
                obj.clicked.connect(partial(self.events.buttonClicked, name))
        self.window.listMenu.itemClicked.connect(self.events.itemClicked)