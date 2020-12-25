import os
from PyQt5 import QtWidgets, QtCore, uic

_percentage = 80

Sources = {
    "create_connection"
}

class BaseDialog(QtWidgets.QDialog):
    cached = True
    def __init__(self, parent = None, ui = None):
        super().__init__(parent)
        if ui is not None:
            uic.loadUi(ui, self)
            
    def fromData(self, data):
        for value in data: # loop over list
            frame = QtWidgets.QFrame()
            layout = QtWidgets.QHBoxLayout()
            frame.setLayout(layout)
            for k, v in value.items(): # loop over each frame (dict)
                if k == "label":
                    label = QtWidgets.QLabel()
                    label.setText(v)
                    layout.addWidget(label)
                elif k == "entry":
                    entry = QtWidgets.QLineEdit(frame)
                    entry.setPlaceholderText(v)
            self.frame_layout.addWidget(frame)
    
    def start(self):
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        
dialog_cache = {}
        
def Dialog(parent = None, ui = None, start = True) -> BaseDialog:
    global dialog_cache
    if isinstance(ui, str):
        if not ui.endswith('.ui'):
            ui = "{ui}.ui".format(ui=ui)
        ui = os.path.join(
            'packet', 'ui', 'dialoguis', ui
        )
    dialog = dialog_cache.get(ui, None)
    if dialog is None:
        dialog = BaseDialog(parent, ui)
        if BaseDialog.cached:
            dialog_cache[ui] = dialog
    if start is True:
        dialog.start()
    return dialog