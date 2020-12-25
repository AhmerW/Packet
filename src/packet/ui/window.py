import os
from PyQt5 import QtWidgets, QtCore, uic

class PacketWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            os.path.join('packet', 'ui', 'window.ui'),
            self
        )
        self.dialog = None

        
    def resizeEvent(self, event):
        if not self.dialog is None:
            self.dialog.close()
            return
        event.accept()