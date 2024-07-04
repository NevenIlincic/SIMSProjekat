from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QScrollArea 
from Model.DTO.EditorsReviewDTO import EditorsReviewDTO
from Model.DTO.GroupFormDTO import GroupFormDTO
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from View.GeneratedFiles.AddParticipantGenerated import Ui_AddParticipant
from PyQt5.QtCore import pyqtSignal, QTimer
from Model.Models.Enumerations import Pol, Zanr
from datetime import datetime
from Model.DTO.ParticipantDTO import ParticipantDTO
from Model.Service.ComplexSerice import ComplexService
from View.GeneratedFiles.AddReviewFormGenerated import Ui_MainWindow

class ReviewForm(QMainWindow, Ui_MainWindow):
    def __init__(self, review_dto: EditorsReviewDTO, user_informations_dto: UserInformationsDTO):
        super().__init__()
        self.setupUi(self)
        self.complex_service = ComplexService()
        self.add_review.clicked.connect(self.add_Review)
        self.review_dto = review_dto
        self.user_informations_dto = user_informations_dto
    def show_message_box(self):
        reply = QMessageBox.question(
            self,
            'Adding review',
            'Are you sure you want to add review?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        return reply

    def add_Review(self):
        description = self.textEdit.toPlainText()
        grade = int(self.gradeComboBox.currentText())
        self.review_dto.ocena = grade
        self.review_dto.opis = description
        message, valid = self.complex_service.validate_data_for_review_adding(self.review_dto)
        if valid == False:
            QMessageBox.information(self, "Message", message)
        else:
            reply = self.show_message_box()
            if reply == QMessageBox.Yes:
                self.complex_service.add_review(self.review_dto, self.user_informations_dto)
                QMessageBox.information(self, "Message", "Review successfully added!")
                self.close()