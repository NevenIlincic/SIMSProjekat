from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.GeneratedFiles.RegisteredUserMainWindowGenerated import Ui_MainWindow
from Model.Service.ComplexSerice import ComplexService
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from PyQt5.QtCore import pyqtSignal

class RegisteredUserMainView(QMainWindow, Ui_MainWindow):
    logout_signal = pyqtSignal()

    def __init__(self, user_dto: UserInformationsDTO):
        super().__init__()
        self.setupUi(self)
        
        self.user_dto = user_dto
        if self.user_dto != None:
            self.show_informations()

        self.pushButton.clicked.connect(self.logout)

    def show_informations(self):
        self.label_2.setText(self.user_dto.korisnicko_ime)
        self.label_4.setText(self.user_dto.lozinka)
        self.label_6.setText(self.user_dto.ime)
        self.label_8.setText(self.user_dto.prezime)
        self.label_10.setText(self.user_dto.pol.value)
        self.label_12.setText(self.user_dto.uloga)

    def logout(self):
        self.logout_signal.emit()
        self.close()