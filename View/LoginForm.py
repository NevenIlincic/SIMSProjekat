from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget
from View.GeneratedFiles.RegisteredUserLoginFormGenerated import Ui_Form
from PyQt5.QtCore import pyqtSignal
from Controller.MusicSupervisorController import MusicSupervisorController
from Model.Models.MuzickiUrednik import MuzickiUrednik
from View.MusicSupervisorView import MusicSupervisorWindow
from Model.Service.ComplexSerice import ComplexService
from View.RegisteredUserMainView import RegisteredUserMainView


class LoginForm(QWidget,Ui_Form):
    cancel_signal = pyqtSignal()

    def __init__(self, role):
        super().__init__()
        self.setupUi(self)
        self.main_window = None
        self.registered_user_window = None


        self.current_role = role
        self.complex_service = ComplexService()
        
        # if (role == "Registered User"):
        #    # self.controller = RegisteredUserController()
        #    pass
        # elif (role == "Music Supervisor"):
        #     self.controller = MusicSupervisorController()
        # else:
        #     #self.controller = AdministratorController()
        #     pass

        # Functions call
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.return_to_main)
        
    
    def return_to_main(self):
        self.cancel_signal.emit()
        self.close()
    
    def login(self):
        password = self.lineEdit.text()
        username = self.lineEdit_2.text()
        if self.current_role == "Registered user":
            dto = self.complex_service.user_login(username, password)
            if dto != None:
                self.registered_user_window = RegisteredUserMainView(dto)
                self.registered_user_window.show()
                self.close()
            else:
                QMessageBox.information(self, "Poruka", "Incorrect username or password!")