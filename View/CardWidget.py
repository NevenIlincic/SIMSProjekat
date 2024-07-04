from View.ParticipantSupervisorView import ParticipantSupervisorWindow
from PyQt5.QtWidgets import QMainWindow
from Model.DTO.EditorsReviewDTO import EditorsReviewDTO
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from View.AddReviewFormView import ReviewForm
from View.GeneratedFiles.MusicSupervisorMenuGenerated import Ui_MainWindow
from Model.Models.Ucesnik import Ucesnik
from Model.Models.MuzickiElement import MuzickiElement
from PyQt5.QtCore import pyqtSignal
from View.AddParticipantView import AddParticipantWindow
from Model.Service.ComplexSerice import ComplexService
from View.GeneratedFiles.CardWidgetGenerated import Ui_CardWidget
import requests
from io import BytesIO
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QScrollArea
class CardWidget(QMainWindow,  Ui_CardWidget):
    update_signal = pyqtSignal()
    def __init__(self, element: MuzickiElement, user_informations_dto:UserInformationsDTO):
        super().__init__()
        self.setupUi(self)
        self.element = element
        self.view_window = None
        self.user_informations_dto = user_informations_dto
        self.label.setText(element.naziv)
        self.element = element
        self.complex_service = ComplexService()
        self.setStyleSheet("""
            QWidget {
                background-color: #e6f7ff;  /* Light blue close to white */
                border: 0.5px solid #00008b;  /* Dark blue border */
                border-radius: 10px;        /* Optional: rounded corners */
            }
            QLabel {
                border: 0px;
            }
            QPushButton {
                background-color: #90ee90;  /* Light green */
                border-radius: 5px;        /* Optional: rounded corners */
            }
            QPushButton:hover {
                background-color: #77dd77;  /* Slightly darker green when hovered */
            }
        """)
        
        self.frame.setFrameShape(QFrame.Box)
        self.set_image_in_frame(self.frame, element.slika)
        self.add_review_window = None
        self.pushButton_2.clicked.connect(self.add_review)
        #Function call
        self.pushButton.clicked.connect(self.view_element)

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
        frame.setLayout(self.frame_layout)

        self.frame.installEventFilter(self)

    def resize_image(self):
        # Resize the image to fit the frame
        frame_width = self.frame.size().width()
        frame_height = self.frame.size().height()
        image = self.image.scaled(frame_width, frame_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(image)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Resize and source is self.frame:
            self.resize_image()
        return super().eventFilter(source, event)
    
    def view_element(self):
        if isinstance(self.element, Ucesnik):
            self.view_window = ParticipantSupervisorWindow(self.element)
            self.view_window.show()
    def add_review(self):  
        message, valid = self.complex_service.check_for_user_review(self.user_informations_dto, self.element)
        if valid == False:
            QMessageBox.information(self, "Message", message)
        else:
            review_dto = EditorsReviewDTO("", 0, self.element)
            self.add_review_window = ReviewForm(review_dto, self.user_informations_dto)
            self.add_review_window.update_signal.connect(self.update_main)
            self.add_review_window.show()

    def update_main(self):
        self.complex_service = ComplexService()
        self.update_signal.emit()
