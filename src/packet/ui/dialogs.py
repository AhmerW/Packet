from PyQt5 import QtWidgets, QtCore

class BaseDialog(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setStyleSheet("background-color: white;")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    
## Input Dialogs ## 

class ClientConnect(BaseDialog):
    def __init__(self):
        pass
