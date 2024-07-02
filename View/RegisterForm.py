from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from View.GeneratedFiles.RegisterFormGenerated import Ui_Dialog
from PyQt5.QtCore import pyqtSignal
from Controller.MusicSupervisorController import MusicSupervisorController
from Model.Models.MuzickiUrednik import MuzickiUrednik
from Model.DTO.UserDTO import UserDTO
from Model.DTO.UserAccountDTO import UserAccountDTO
from View.MusicSupervisorView import MusicSupervisorWindow
from Model.Service.ComplexSerice import ComplexService
from View.RegisteredUserHomeView import RegisteredUserHomeView
from Model.Models.Enumerations import Pol, VrstaKorisnika


class RegisterForm(QWidget,Ui_Dialog):
    cancel_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_window = None
        self.registered_user_window = None
        self.supervisor_window = None
        self.complex_service = ComplexService()        
        self.pushButton_3.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.return_to_login_form)
        
    def return_to_login_form(self):
        self.cancel_signal.emit()
        self.close()
    
    def register(self):
        name = self.lineEdit_2.text()
        surname = self.lineEdit_3.text()
        username = self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        gender = self.comboBox.currentText()
        if (gender == "musko"):
            gender = Pol.Muski
        else:
            gender = Pol.Zenski

        user_dto = UserDTO(name, surname, gender, None)
        user_account_dto = UserAccountDTO(username, password, VrstaKorisnika.Registrovani_korisnik)

        message, valid = self.complex_service.validate_data_for_registration(user_dto, user_account_dto)
        if not valid:
            QMessageBox.information(self, "Error", message)
            return
        else:
            self.complex_service.register_new_user(user_dto, user_account_dto)
            QMessageBox.information(self, "Registration done", "You registered to application")
            self.return_to_login_form()




      