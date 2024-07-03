from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.GeneratedFiles.AddParticipantGenerated import Ui_AddParticipant
from PyQt5.QtCore import pyqtSignal, QTimer
from Model.Models.Enumerations import Pol, Zanr
from datetime import datetime
from Model.DTO.ParticipantDTO import ParticipantDTO
from Model.Service.ComplexSerice import ComplexService

class AddParticipantWindow(QMainWindow, Ui_AddParticipant):
    logout_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.complex_service = ComplexService()
        self.show_informations()
        #Function call
        self.save_button.clicked.connect(self.save)

    def show_informations(self):
        for gender in Pol:
            self.gender_combo.addItem(gender.name, gender.value)

    def error_box(self, title, text, info):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setInformativeText(info)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def validate_data(self):
        if self.artname_edit.text() == "":
            self.error_box("Error", "Some boxes are left empty.", "You have not written artistic name.")
            return
        if self.fname_edit.text() == "":
            self.error_box("Error", "Some boxes are left empty.", "You have not written first name.")
            return
        if self.lname_edit.text() == "":
            self.error_box("Error", "Some boxes are left empty.", "You have not written last name.")
            return
        if self.image_edit.text() == "":
            self.error_box("Error", "Some boxes are left empty.", "You have not written image url.")
            return
        if self.biography_edit.toPlainText() == "":
            self.error_box("Error", "Some boxes are left empty.", "You have not written biography.")
            return
        if not (self.folk_check.isChecked() or self.pop_check.isChecked() or self.classic_check.isChecked() or self.jazz_check.isChecked()):
            self.error_box("Error", "No genre selected.", "You have not selected any genre.")
            return
        return True

    def save(self):
        if self.validate_data():
            art_name = self.artname_edit.text()
            first_name = self.fname_edit.text()
            last_name = self.lname_edit.text()
            image_url = self.image_edit.text()
            biography = self.biography_edit.toPlainText()

            datum_str = self.datepicker.date().toString("yyyy-MM-dd")
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()

            lista = []
            if self.folk_check.isChecked(): lista.append(Zanr.Narodna)
            if self.pop_check.isChecked(): lista.append(Zanr.Pop)
            if self.classic_check.isChecked(): lista.append(Zanr.Klasika)
            if self.jazz_check.isChecked(): lista.append(Zanr.Dzez)

            gender = Pol(self.gender_combo.currentText().lower())

            participant = ParticipantDTO(0, art_name, image_url, 0, 0, 0, first_name,
                                         last_name, gender, datum,
                                         biography, lista, False)
            
            self.complex_service.add_new_participant(participant)
            QMessageBox.information(self, "Participant added", "You have added new participant")
            self.close()

        