from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from View.GeneratedFiles.RegisterFormGenerated import Ui_Dialog
from PyQt5.QtCore import pyqtSignal
from Controller.MusicSupervisorController import MusicSupervisorController
from Model.Models.MuzickiUrednik import MuzickiUrednik
from View.MusicSupervisorView import MusicSupervisorWindow
from Model.Service.ComplexSerice import ComplexService
from View.RegisteredUserHomeView import RegisteredUserHomeView



class RegisterForm(QWidget,Ui_Dialog):
    cancel_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_window = None
        self.registered_user_window = None
        self.supervisor_window = None
        self.complex_service = ComplexService()
        
        # if (role == "Registered User"):
    
        self.pushButton_3.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.return_to_login_form)
        

    def return_to_login_form(self):
        self.cancel_signal.emit()
        self.close()
    
    def register(self):
        pass

      