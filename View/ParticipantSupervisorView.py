from io import BytesIO
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.AddMusicalPieceFormView import AddMusicalPieceWindow
from View.GeneratedFiles.ParticipantSupervisorViewGenerated import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from Model.Models.Ucesnik import Ucesnik
from View.AddParticipantView import AddParticipantWindow
from Model.Service.ComplexSerice import ComplexService
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QEvent
import requests

class ParticipantSupervisorWindow(QMainWindow,  Ui_MainWindow):
    def __init__(self, participant: Ucesnik):
        super().__init__()
        self.setupUi(self)
        self.complex = ComplexService()
        self.participant = participant
        self.show_informations()
        #Function call

    def show_informations(self):
        self.artist_label.setText(self.participant.naziv)
        self.fname_label.setText(self.participant.ime)
        self.lname_label.setText(self.participant.prezime)
        self.date_label.setText(self.participant.datum_rodjenja.strftime("%d.%m.%Y"))
        self.gender_label.setText(self.participant.pol.value)
        self.biography_label.setText(self.participant.biografija)

        grade = round(self.participant.zbir_ocena / self.participant.broj_ocena, 1)
        self.grade_label.setText(str(grade))
        self.ratings_label.setText("from "+str(self.participant.broj_ocena)+" ratings")
        if grade >= 4.9:
            self.stars_label.setText("🌕🌕🌕🌕🌕")
        elif grade >= 4.4:
            self.stars_label.setText("🌕🌕🌕🌕🌗")
        elif grade >= 3.9:
            self.stars_label.setText("🌕🌕🌕🌕🌑")
        elif grade >= 3.4:
            self.stars_label.setText("🌕🌕🌕🌗🌑")
        elif grade >= 2.9:
            self.stars_label.setText("🌕🌕🌕🌑🌑")
        elif grade >= 2.4:
            self.stars_label.setText("🌕🌕🌗🌑🌑")
        elif grade >= 1.9:
            self.stars_label.setText("🌕🌕🌑🌑🌑")
        elif grade >= 1.4:
            self.stars_label.setText("🌕🌗🌑🌑🌑")
        else:
            self.stars_label.setText("🌕🌑🌑🌑🌑")

        genres_string = ""
        for genre in self.participant.zanrovi:
            genres_string += genre.value
            if genre != self.participant.zanrovi[-1]:
                genres_string += ", "
        self.genres_label.setText(genres_string)

        self.set_image_in_frame(self.image_frame, self.participant.slika)

        if genres_string.find("Klasika") != -1:
            self.setStyleSheet("""
                QWidget#banner_widget {
                    background: qlineargradient(
                        x1: 0, y1: 1, x2: 0, y2: 0,
                        stop: 0 darkred, stop: 1 red
                    );
                }
                QMainWindow {
                    background-color: #ffebeb;
                }
            """)
        elif genres_string.find("Pop") != -1:
            self.setStyleSheet("""
                QWidget#banner_widget {
                    background: qlineargradient(
                        x1: 0, y1: 1, x2: 0, y2: 0,
                        stop: 0 darkpurple, stop: 1 purple
                    );
                }
                QMainWindow {
                    background-color: #f9ebff;
                }
            """)
        elif genres_string.find("Dzez") != -1:
            self.setStyleSheet("""
                QWidget#banner_widget {
                    background: qlineargradient(
                        x1: 0, y1: 1, x2: 0, y2: 0,
                        stop: 0 darkblue, stop: 1 blue
                    );
                }
                QMainWindow {
                    background-color: #ebeeff;
                }
            """)
        elif genres_string.find("Narodna") != -1:
            self.setStyleSheet("""
                QWidget#banner_widget {
                    background: qlineargradient(
                        x1: 0, y1: 1, x2: 0, y2: 0,
                        stop: 0 darkgreen, stop: 1 green
                    );
                }
                QMainWindow {
                    background-color: #ebffec;
                }
            """)

    def set_image_in_frame(self, frame, image_url):
        # Download the image from the URL
        response = requests.get(image_url)
        self.image = QPixmap()
        self.image.loadFromData(BytesIO(response.content).read())

        # Create a QLabel to display the image
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.resize_image()

        # Add the QLabel to the QFrame's layout
        self.frame_layout = QVBoxLayout()
        self.frame_layout.addWidget(self.image_label)
        self.image_frame.setLayout(self.frame_layout)

        self.image_frame.installEventFilter(self)

    def resize_image(self):
        # Resize the image to fit the frame
        frame_width = self.image_frame.size().width()
        frame_height = self.image_frame.size().height()
        image = self.image.scaled(frame_width, frame_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(image)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Resize and source is self.image_frame:
            self.resize_image()
        return super().eventFilter(source, event)