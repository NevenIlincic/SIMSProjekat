from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from PyQt5.QtWidgets import QApplication
from Model.DTO.UserAccountDTO import UserAccountDTO
from Model.DTO.UserDTO import UserDTO
from Model.Models.Enumerations import Pol, VrstaKorisnika
from Model.Service.ComplexSerice import ComplexService
from View.GeneratedFiles.AdministratorAddSupervisorGenerated import Ui_Dialog
from PyQt5.QtCore import pyqtSignal

class AdministratorAddSupervisorForm(QDialog, Ui_Dialog):
    cancel_signal = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.complex_service = ComplexService()

        self.pushButton.clicked.connect(self.register_supervisor)
        self.pushButton_2.clicked.connect(self.return_to_main)

    def return_to_main(self):
        self.cancel_signal.emit()
        self.close()
    
    def register_supervisor(self):
        first_name = self.lineEdit.text()
        last_name = self.lineEdit_2.text()
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        gender = self.comboBox.currentText()
        if gender == "Male":
            gender = Pol.Muski
        else:
            gender = Pol.Zenski
        
        user_dto = UserDTO(first_name, last_name, gender, None)
        user_account_dto = UserAccountDTO(username, password, VrstaKorisnika.Urednik)

        message, valid = self.complex_service.validate_data_for_registration(user_dto, user_account_dto)
        if not valid:
            QMessageBox.information(self, "Error", message)
            return
        else:
            self.complex_service.register_new_supervisor(user_dto, user_account_dto)
            QMessageBox.information(self, "Registration done", "Supervisor successfully registered!")
            self.return_to_main()
