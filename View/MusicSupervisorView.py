from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.AddAlbumFormView import AlbumForm
from View.AddMusicalPieceFormView import AddMusicalPieceWindow
from View.GeneratedFiles.MusicSupervisorMenuGenerated import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from PyQt5.QtCore import pyqtSignal
from View.AddParticipantView import AddParticipantWindow
from Model.Service.ComplexSerice import ComplexService
from View.CardWidget import CardWidget
from View.AddGroupFormView import GroupForm

class MusicSupervisorWindow(QMainWindow,  Ui_MainWindow):
    logout_signal = pyqtSignal()
    def __init__(self, dto: UserInformationsDTO):
        super().__init__()
        self.setupUi(self)
        self.complex = ComplexService()
        participants = self.complex.participant_controller.get_all_participants()[:3]

        for participant in participants:
            card = CardWidget(participant, dto)
            self.artist_layout_2.addWidget(card)

        self.add_participant_window = None
        self.add_musical_piece_window = None
        self.add_group_window = None
        self.add_album_window = None

        self.supervisor_dto = dto
        self.show_informations()

        #Function call
        self.pushButton.clicked.connect(self.logout)
        self.participant_button.clicked.connect(self.add_participant)
        self.piece_button.clicked.connect(self.add_musical_piece)
        self.group_button.clicked.connect(self.add_group)
        self.album_button.clicked.connect(self.add_album)

    def show_informations(self):
        self.title_label.setText("Welcome back, "+self.supervisor_dto.ime+" "+self.supervisor_dto.prezime+"!")
        
    def logout(self):
        self.logout_signal.emit()
        self.close()
        
    def add_participant(self):
        self.add_participant_window = AddParticipantWindow()
        self.add_participant_window.show()

    def add_musical_piece(self):
        self.add_musical_piece_window = AddMusicalPieceWindow()
        self.add_musical_piece_window.show()

    def add_group(self):
        self.add_group_window = GroupForm()
        self.add_group_window.show()

    def add_album(self):
        self.add_album_window = AlbumForm()
        self.add_album_window.show()
