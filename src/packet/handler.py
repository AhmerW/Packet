from functools import partial
from typing import List 
import os
from PyQt5 import QtWidgets, QtCore


from packet.common.singleton import Singleton
from packet.ui.window import PacketWindow
from packet.lib.network import Listener

from packet.ui.dialogs import Dialog
from packet.common.validators import Regex, validateEntries

mapped = {
    "news": 1,
    "create_a_connection": (3, "connectionHandling")
}


class Events(object):
    def __init__(self, window, user):
        self.window = window
        self.user = user
    

        
    def connectionHandling(self, event):
        def processConnection():
            validated = validateEntries({
                obj.entry_port: Regex.integer_only,
                obj.entry_id: Regex.integer_only
            })
            print(validated)
        if event == 'create_a_connection':
            obj = Dialog(self.window, 'create_connection', start=False, callback = processConnection)
            obj.start()
     
        
    # events

    def itemClicked(self, obj, col):
        text = obj.text(col).lower().replace(' ', '_')
        data = mapped.get(
            text, 
            list()
        )
        if not isinstance(data, list) and not isinstance(data, tuple):
            data = [data]
        func, index = None, 0
        for value in data:
            if isinstance(value, int):
                index = value 
            elif callable(value) or isinstance(value, str):
                func = value
        
        if not index is None:   
            self.window.mainFrame.setCurrentIndex(index)
            
        if isinstance(func, str):
            func = getattr(self, func)
        if callable(func):
            func(text)

      
        
    def buttonClicked(self, button):
        pass

class EventHandler(object, metaclass = Singleton):
    def __init__(self, packet):
        self.packet = packet
        self._cli = packet.cli
        self.app : QtWidgets.QApplication = None
        self.window : PacketWindow = None
        self.events : Events = None
        self.user = packet.user
        
    def loadWindow(self):
        self.app = QtWidgets.QApplication([])
        self.window = PacketWindow()
        self.events = Events(self.window, self.user)
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