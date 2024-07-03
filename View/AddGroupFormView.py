from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.GeneratedFiles.AddParticipantGenerated import Ui_AddParticipant
from PyQt5.QtCore import pyqtSignal, QTimer
from Model.Models.Enumerations import Pol, Zanr
from datetime import datetime
from Model.DTO.ParticipantDTO import ParticipantDTO
from Model.Service.ComplexSerice import ComplexService
from View.GeneratedFiles.AddGroupFormGenerated import Ui_MainWindow

class GroupForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.complex_service = ComplexService()

        self.cancelButton.clicked.connect(self.cancel_window)
        self.searchButton.clicked.connect(self.search_participant)
        
    def search_participant(self):
        first_name = self.participantFirstName.text()
        last_name = self.participantLastName.text()

    def cancel_window(self):
        self.close()