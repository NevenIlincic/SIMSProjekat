from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.GeneratedFiles.MusicSupervisorMenuGenerated import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal

class MusicSupervisorWindow(QMainWindow,  Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.main_window = None

        #Function call
        self.pushButton.clicked.connect(self.logout)

    def logout(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()
        