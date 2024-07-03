from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.GeneratedFiles.MusicSupervisorMenuGenerated import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from PyQt5.QtCore import pyqtSignal
from View.AddParticipantView import AddParticipantWindow

class MusicSupervisorWindow(QMainWindow,  Ui_MainWindow):
    logout_signal = pyqtSignal()
    def __init__(self, dto: UserInformationsDTO):
        super().__init__()
        self.setupUi(self)

        self.add_participant_window = None

        self.supervisor_dto = dto
        self.show_informations()
        #Function call
        self.pushButton.clicked.connect(self.logout)
        self.participant_button.clicked.connect(self.add_participant)

    def show_informations(self):
        self.title_label.setText("Welcome back, "+self.supervisor_dto.ime+" "+self.supervisor_dto.prezime+"!")
        
    def logout(self):
        self.logout_signal.emit()
        self.close()
        
    def add_participant(self):
        self.add_participant_window = AddParticipantWindow()
        self.add_participant_window.show()

    # def add_musical_piece(self):
    #     self.add_musical_piece_window = AddMusicalPieceWindow()
    #     self.add_musical_piece_window.show()