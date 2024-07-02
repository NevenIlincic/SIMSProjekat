# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\RegisteredUserHomeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from View.GeneratedFiles.RegisteredUserHomeWindowGenerated import Ui_MainWindow
from Model.Service.ComplexSerice import ComplexService
from Model.DTO.UserInformationsDTO import UserInformationsDTO
from PyQt5.QtCore import pyqtSignal


class RegisteredUserHomeView(QMainWindow, Ui_MainWindow):
    logout_signal = pyqtSignal()

    def __init__(self, user_dto: UserInformationsDTO):
        super().__init__()
        self.setupUi(self) 
        self.user_dto = user_dto

        self.title_label.setText( "Welcome back, "+user_dto.ime+" "+user_dto.prezime+"!")
        self.pushButton.clicked.connect(self.logout)
    
    def logout(self):
        self.logout_signal.emit()
        self.close()
