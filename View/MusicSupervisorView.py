from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.GeneratedFiles.MusicSupervisorMenuGenerated import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from PyQt5.QtCore import pyqtSignal

class MusicSupervisorWindow(QMainWindow,  Ui_MainWindow):
    logout_signal = pyqtSignal()
    def __init__(self, dto: UserInformationsDTO):
        super().__init__()
        self.setupUi(self)

        self.supervisor_dto = dto
        self.show_informations()
        #Function call
        self.pushButton.clicked.connect(self.logout)

    def show_informations(self):
        self.label_2.setText(self.supervisor_dto.korisnicko_ime)
        self.label_4.setText(self.supervisor_dto.lozinka)
        self.label_6.setText(self.supervisor_dto.ime)
        self.label_8.setText(self.supervisor_dto.prezime)
        self.label_10.setText(self.supervisor_dto.pol.value)
        self.label_12.setText(self.supervisor_dto.uloga)
        
    def logout(self):
        self.logout_signal.emit()
        self.close()
        