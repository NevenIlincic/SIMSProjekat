from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from View.GeneratedFiles.MusicSupervisorMenuGenerated import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from Model.Models.MuzickiElement import MuzickiElement
from PyQt5.QtCore import pyqtSignal
from View.AddParticipantView import AddParticipantWindow
from Model.Service.ComplexSerice import ComplexService
from View.GeneratedFiles.WidgetForListGenerated import Ui_WidgetForList
from Model.Models.ListaOmiljenih import ListaOmiljenih
import requests
from io import BytesIO
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QEvent

class WidgetForList(QMainWindow,  Ui_WidgetForList):
    def __init__(self, element: MuzickiElement, list_of_favourites : ListaOmiljenih):
        super().__init__()
        self.setupUi(self)
        self.list_of_favourites = list_of_favourites
        self.label.setText(element.naziv)
        
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
    
        #Function call
        self.pushButton.clicked.connect(self.add_to_list)

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
    
    def add_to_list(self):
        pass