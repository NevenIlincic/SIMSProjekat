from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtWidgets import QApplication
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from View.GeneratedFiles.AdministratorMainWindowGenerated import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from View.AdministratorAddSupervisorForm import AdministratorAddSupervisorForm

class AdministratorMainView(QMainWindow, Ui_MainWindow):
    logout_signal = pyqtSignal()

    def __init__(self, dto: UserInformationsDTO) -> None:
        super().__init__()
        self.setupUi(self)
        self.supervisor_register_form = None

        self.administrator_dto = dto

        self.pushButton.clicked.connect(self.logout)
        self.pushButton_2.clicked.connect(self.open_supervisor_register_form)
        self.title_label.setText("Welcome back, "+self.administrator_dto.ime+" "+self.administrator_dto.prezime+"!")

    def logout(self):
        self.logout_signal.emit()
        self.close()
    
    def open_supervisor_register_form(self):
        self.supervisor_register_form = AdministratorAddSupervisorForm()
        self.supervisor_register_form.cancel_signal.connect(self.handle_cancel)
        self.supervisor_register_form.show()
        self.close()

    def handle_cancel(self):
        self.show()