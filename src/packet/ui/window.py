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
        self.dialog_redraw = False 
        self.listMenu.setContentsMargins(0, 0, 0, 0)

    def closeCurrentDialog(self, func = None):
        self.centralWidget().setDisabled(False)
        self.dialog.close()
        self.dialog = None
        if callable(func): func()
               
    def resizeEvent(self, event):
        if not self.dialog is None:
            if not self.dialog_redraw:
                return self.closeCurrentDialog()
            else:
                self.dialog.moveCenter()
        event.accept()