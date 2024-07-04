from io import BytesIO
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.AddMusicalPieceFormView import AddMusicalPieceWindow
from View.GeneratedFiles.PieceSupervisorViewGenerated import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from Model.Models.MuzickoDelo import MuzickoDelo
from Model.Service.ComplexSerice import ComplexService
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QEvent
import requests
import random

class PieceSupervisorWindow(QMainWindow,  Ui_MainWindow):
    def __init__(self, piece: MuzickoDelo):
        super().__init__()
        self.setupUi(self)
        self.complex = ComplexService()
        self.piece = piece
        self.show_informations()
        #Function call

    def show_informations(self):
        self.piece_label.setText(self.piece.naziv)
        self.lyrics_browser.setText(self.piece.tekst)

        grade = 2.5
        if self.piece.broj_ocena > 0:
            grade = round(self.piece.zbir_ocena / self.piece.broj_ocena, 1)
        self.grade_label.setText(str(grade))
        self.ratings_label.setText("from "+str(self.piece.broj_ocena)+" ratings")
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

        self.set_image_in_frame(self.image_frame, self.piece.slika)

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
            QPushButton#favourite_button {
            background-color: #90ee90;  /* Light green */
            border-radius: 5px;        /* Optional: rounded corners */
            }
            QPushButton:hover#favourite_button {
                background-color: #77dd77;  /* Slightly darker green when hovered */
            }
        """)

        
        reviews = self.complex.editors_review_controller.get_reviews_by_music_element(self.piece)
        if len(reviews):
            self.review_button.setVisible(False)
            review = random.choice(reviews)
            self.textBrowser.setText(review.opis)
        else:
            self.editor_title_label.setVisible(False)
            self.textBrowser.setText("No review has been made yet by supervisors!")

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