from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.GeneratedFiles.AddParticipantGenerated import Ui_AddParticipant
from PyQt5.QtCore import pyqtSignal, QTimer
from Model.Models.Enumerations import Pol, Zanr
from datetime import datetime
from Model.DTO.ParticipantDTO import ParticipantDTO
from Model.Service.ComplexSerice import ComplexService
from View.GeneratedFiles.AddMusicalPieceFormGenerated import Ui_MainWindow
class AddMusicalPieceWindow(QMainWindow, Ui_MainWindow):
    logout_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.complex_service = ComplexService()
        # self.show_informations()
        # #Function call
        # self.save_button.clicked.connect(self.save)