from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.RegisteredUserView import RegisteredUserWindow
import sys
from PyQt5.QtWidgets import QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/startingMenu.ui', self)
        
        # Povezivanje dugmeta sa funkcijom
        self.user_view = None
        self.administrator_view = None
        self.music_superviser_view = None
        self.pushButton.clicked.connect(self.open_user_menu)


    def open_user_menu(self):
        self.user_view = RegisteredUserWindow()
        self.user_view.show()
        self.close()
       
