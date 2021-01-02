import os
from PyQt5 import QtWidgets, QtCore, uic
from packet.common.validators import Regex
from packet.ui.errors import errorBox

_percentage = 80

Sources = {
    "create_connection"
}

class BaseDialog(QtWidgets.QDialog):
    cached = False
    def __init__(self, parent = None, ui = None, callback = None ):
        super().__init__(parent)
        if ui is not None:
            uic.loadUi(ui, self)
        self.callback = callback
        self.close_on_continue = True
        self.error_text = "Invalid input."
        self.button_ok.clicked.connect(self.clickedContinue)
        self.button_cancel.clicked.connect(self.close)
        self.stylesheet = \
            """
            font-size: 20px;
            """
        self._entry_validators = {}
        
    def closeEvent(self, event):
        event.accept()
        
    def clickedContinue(self):
        validated = True 
        for entry, rgx in self._entry_validators.items():
            if not Regex.match(rgx, entry.text()):
                validated = False 
                break
        if not validated:
            errorBox(text=self.error_text)
        if self.close_on_continue:
            self.close()
        if callable(self.callback):
            self.callback()


            
    def fromData(self, data, return_widgets = True):
        self.setStyleSheet(self.stylesheet)
        widgets = []
        for value in data: # loop over list
            frame = QtWidgets.QFrame()
            frame.setMaximumHeight(len(value)*100)
            layout = QtWidgets.QVBoxLayout()
            frame.setLayout(layout)
            for k, v in value.items(): # loop over each frame (dict)
                if k.startswith("label"):
                    label = QtWidgets.QLabel(frame)
                    label.setText(v)
                    layout.addWidget(label)
                    widgets.append(label)
                elif k.startswith("entry"):
                    if isinstance(v, list):
                        text, regex = v 
                    else:
                        text = v
                    entry = QtWidgets.QLineEdit(frame)
                    entry.setPlaceholderText(text)
                    entry.setObjectName(k)
                    layout.addWidget(entry)
                    self._entry_validators[entry] = regex
                    widgets.append(entry)

            self.frame_layout.addWidget(frame)
            if return_widgets:
                return widgets
    
    def start(self):
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()

        
dialog_cache = {}
        
def Dialog(parent = None, ui = None, callback = None, start = True) -> BaseDialog:
    global dialog_cache
    if isinstance(ui, str):
        if not ui.endswith('.ui'):
            ui = "{ui}.ui".format(ui=ui)
        ui = os.path.join(
            'packet', 'ui', 'dialoguis', ui
        )
    dialog = dialog_cache.get(ui, None)
    if dialog is None:
        dialog = BaseDialog(parent, ui, callback)
        if BaseDialog.cached:
            dialog_cache[ui] = dialog
    if start is True:
        dialog.start()
    return dialog