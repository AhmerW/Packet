import os
from PyQt5 import QtWidgets, uic

class PacketWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            os.path.join('packet', 'ui', 'window.ui'),
            self
        )