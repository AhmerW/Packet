from PyQt5.QtWidgets import QMessageBox



def errorBox(text, title = "Error", informative = None):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Critical)
    msg.setText(text)
    if not informative is None:
        msg.setInformativeText(informative)
    msg.exec_()