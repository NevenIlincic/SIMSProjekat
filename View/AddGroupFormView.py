from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QScrollArea
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

        self.selected_participants = set()

        self.cancelButton.clicked.connect(self.cancel_window)
        self.searchButton.clicked.connect(self.search_participant)
        self.addParticipantButton.clicked.connect(self.add_participant)

    
    def search_participant(self):
        duplicate_participants = []
        first_name = self.participantFirstName.text()
        last_name = self.participantLastName.text()
        pseudonym = self.participantPseudonym.text()
        participant, participant_by_pseudonym, participants_first_name, participants_last_name = self.complex_service.participant_controller.get_participants_first_last_name_pseudonym(first_name, last_name, pseudonym) 

        if participant != None:
            duplicate_participants.append(participant)
        if participant_by_pseudonym != None:
            duplicate_participants.append(participant_by_pseudonym)

        duplicate_participants.extend(participants_first_name)
        duplicate_participants.extend(participants_last_name)

        found_participants = set(duplicate_participants)
        for found_participant in found_participants:
            self.listView.addItem(found_participant.ime+" "+found_participant.prezime + "-"+found_participant.naziv)

    def add_participant(self):
        pseudonym = self.listView.text().split("-")[1]
        participant = self.complex_service.participant_controller.get_by_pseodonym(pseudonym)
        self.selected_participants.add()

    def cancel_window(self):
        self.close()