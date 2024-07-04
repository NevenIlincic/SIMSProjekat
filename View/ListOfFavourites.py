from PyQt5.QtCore import pyqtSignal
from View.AddParticipantView import AddParticipantWindow
from Model.Service.ComplexSerice import ComplexService
from View.WidgetForList import WidgetForList
from Controller import MusicalElementController
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget
from View.GeneratedFiles.ListOfFavouritesGenerated import Ui_Dialog
from Model.DTO.ListOfFavouritesDTO import ListaOmiljenihDTO

class ListOfFavourites(QWidget,  Ui_Dialog):
    cancel_signal = pyqtSignal()

    def __init__(self, username : str):
        super().__init__()
        self.setupUi(self)
        self.complex = ComplexService()
        self.musical_piece_controller = self.complex.musical_element_controller
        self.list_controller = self.complex.list_controller
        self.user_controller = self.complex.registered_account_controller
        self.username = username
        self.list_of_songs = []  # Lista za pohranu odabranih pjesama
        self.id_list = None  # Inicijalizacija varijable za ID liste

        lista_dela=[]
        elements = self.musical_piece_controller.get_all_elements()
        list_of_favourites_songs = ListaOmiljenihDTO(0, "", self.user_controller.get_by_username(username), lista_dela)
        list_of_favourites = self.list_controller.add_list(list_of_favourites_songs)
        self.id_list = list_of_favourites.id

        for element in elements:
            card = WidgetForList(element, list_of_favourites)
            self.artist_layout_2.addWidget(card)
            # Povezivanje signala widgetButton s slotom store_selected_song
            card.pushButton.clicked.connect(lambda checked, elem=element: self.store_selected_song(elem))

        self.pushButton.clicked.connect(self.make_list)
        self.pushButton_2.clicked.connect(self.return_to_main_window)

    def store_selected_song(self, selected_element):
        # Dodavanje odabranog elementa u listu self.list_of_songs
        self.list_of_songs.append(selected_element)

    def return_to_main_window(self):
        if self.list_of_songs and len(self.list_of_songs) == 0:
            self.list_controller.delete_list(self.id_list)
        self.cancel_signal.emit()
        self.close()

    def make_list(self):
        if not self.lineEdit.text():
            QMessageBox.information(self, "Error", "List name is empty")
            return

        if not self.list_of_songs:
            QMessageBox.information(self, "Error", "You have to choose at least one song")
            return

        list_of_favourites = self.list_controller.get_by_id(self.id_list)
        list_of_favourites.naziv = self.lineEdit.text()
        list_of_favourites.muzicki_elementi = self.list_of_songs
        self.list_controller.update_list(list_of_favourites)

        QMessageBox.information(self, "Success", "List created successfully")
        self.cancel_signal.emit()
        self.close()
        
        

        #napraviti listu za korisnika sa delima
        #prikazati tu listu na glavnom prozoru
        
        
  