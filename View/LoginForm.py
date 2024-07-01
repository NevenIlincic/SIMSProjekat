from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget
from View.GeneratedFiles.RegisteredUserLoginFormGenerated import Ui_Form
from PyQt5.QtCore import pyqtSignal
from Controller.MusicSupervisorController import MusicSupervisorController
from Model.Models import MuzickiUrednik
from View import MusicSupervisorView

class LoginForm(QWidget,Ui_Form):
    cancel_signal = pyqtSignal()

    def __init__(self, role):
        super().__init__()
        self.setupUi(self)
        self.main_window = None
        self.supervisor_window = None

        self.current_role = role
        self.controller = None
        
        if (role == "Registered User"):
           # self.controller = RegisteredUserController()
           pass
        elif (role == "Music Supervisor"):
            self.controller = MusicSupervisorController()
        else:
            #self.controller = AdministratorController()
            pass

        # Functions call
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.return_to_main)
        
        self.name = self.lineEdit.text()
        self.lastName = self.lineEdit_2.text()
    
    def return_to_main(self):
        self.cancel_signal.emit()
        self.close()
    
    def login(self):
        registered_person = self.controller.login(self.name, self.lastName)
        if registered_person == False:
            QMessageBox.information(self, "Poruka", self.name)
        if type(registered_person) == MuzickiUrednik:
            self.supervisor_window = MusicSupervisorView()
            self.supervisor_window.show()
            self.close()
