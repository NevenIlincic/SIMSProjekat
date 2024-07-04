from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QScrollArea
from Model.DTO.AlbumFormDTO import AlbumFormDTO
from Model.DTO.GroupFormDTO import GroupFormDTO
from View.GeneratedFiles.AddParticipantGenerated import Ui_AddParticipant
from PyQt5.QtCore import pyqtSignal, QTimer
from Model.Models.Enumerations import Pol, Zanr
from datetime import datetime
from Model.DTO.ParticipantDTO import ParticipantDTO
from Model.Service.ComplexSerice import ComplexService
from View.GeneratedFiles.AddAlbumFormGenerated import Ui_MainWindow

class AlbumForm(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.complex_service = ComplexService()

        self.selected_pieces = set()

        self.cancelButton.clicked.connect(self.cancel_window)
        self.addPieceButton.clicked.connect(self.add_musical_piece)
        self.add_button.clicked.connect(self.add_album)
        

        self.fullfill_list()

    def fullfill_list(self):
        for piece in self.complex_service.music_piece_controller.get_all_pieces():
            self.listView.addItem(piece.naziv)

    def add_musical_piece(self):
        if self.listView.currentItem() == None:
            QMessageBox.information(self, "Message", "Select piece first first!")
        else:
            piece_name = self.listView.currentItem().text()
            piece = self.complex_service.music_piece_controller.get_by_name(piece_name)
            self.selected_pieces.add(piece)

    def add_album(self):
        album_name = self.albumName.text()
        image_url = self.imageUrl.text()
        album_dto = AlbumFormDTO(album_name, image_url, self.selected_pieces)
        message, valid = self.complex_service.validate_data_for_album_adding(album_dto)
        if valid == False:
            QMessageBox.information(self, "Message", message)
        else:
            self.complex_service.album_controller.add_album(album_dto)
            QMessageBox.information(self, "Message", "Album successfully created!")
            self.close()

    def cancel_window(self):
        self.close()