from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.MusicSupervisorView import MusicSupervisorWindow
from PyQt5.QtWidgets import QApplication
from View.GeneratedFiles.StartingMenuGenerated import Ui_MainWindow
from View.LoginForm import LoginForm

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Povezivanje dugmeta sa funkcijom
        self.user_login_form = None
        self.administrator_login_form = None
        self.music_supervisor_login_form = None

        ##Pozivanje funkcija
        self.pushButton.clicked.connect(self.open_supervisor_menu)


    def open_supervisor_menu(self):
        self.user_login_form = LoginForm("Music Supervisor")
        self.user_login_form.cancel_signal.connect(self.handle_cancel)
        self.user_login_form.show()
        self.close()
       
    def handle_cancel(self):
        self.show()