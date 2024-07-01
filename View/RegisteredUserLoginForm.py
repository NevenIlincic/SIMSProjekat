from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget


class RegisteredUserLoginForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/RegisteredUserLoginForm.ui', self)
    
        self.pushButton.clicked.connect("Nesto")
        