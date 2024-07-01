from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.GeneratedFiles.RegisteredUserMainWindowGenerated import Ui_MainWindow
from Model.Service.ComplexSerice import ComplexService
from Model.DTO.UserInformationsDTO import UserInformationsDTO

class RegisteredUserMainView(QMainWindow, Ui_MainWindow):
    def __init__(self, user_dto: UserInformationsDTO):
        super().__init__()
        self.setupUi(self)
        
        self.user_dto = user_dto
        self.show_informations()
    
    def show_informations(self):
        self.label_2.setText(self.user_dto.korisnicko_ime)
        self.label_4.setText(self.user_dto.lozinka)
        self.label_6.setText(self.user_dto.ime)
        self.label_8.setText(self.user_dto.prezime)
        self.label_10.setText(self.user_dto.pol.value)
        self.label_12.setText(self.user_dto.uloga)
