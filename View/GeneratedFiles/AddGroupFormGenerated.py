# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/AddGroupForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupName = QtWidgets.QLineEdit(self.centralwidget)
        self.groupName.setGeometry(QtCore.QRect(10, 80, 581, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.groupName.setFont(font)
        self.groupName.setText("")
        self.groupName.setAlignment(QtCore.Qt.AlignCenter)
        self.groupName.setClearButtonEnabled(False)
        self.groupName.setObjectName("groupName")
        self.imageUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.imageUrl.setGeometry(QtCore.QRect(10, 130, 581, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.imageUrl.setFont(font)
        self.imageUrl.setText("")
        self.imageUrl.setAlignment(QtCore.Qt.AlignCenter)
        self.imageUrl.setClearButtonEnabled(False)
        self.imageUrl.setObjectName("imageUrl")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(10, 480, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.participantList = QtWidgets.QListWidget(self.centralwidget)
        self.participantList.setGeometry(QtCore.QRect(270, 230, 311, 91))
        self.participantList.setObjectName("participantList")
        self.addParticipantButton = QtWidgets.QPushButton(self.centralwidget)
        self.addParticipantButton.setGeometry(QtCore.QRect(10, 280, 141, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.addParticipantButton.setFont(font)
        self.addParticipantButton.setObjectName("addParticipantButton")
        self.participantFirstName = QtWidgets.QLineEdit(self.centralwidget)
        self.participantFirstName.setGeometry(QtCore.QRect(60, 180, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.participantFirstName.setFont(font)
        self.participantFirstName.setText("")
        self.participantFirstName.setAlignment(QtCore.Qt.AlignCenter)
        self.participantFirstName.setClearButtonEnabled(False)
        self.participantFirstName.setObjectName("participantFirstName")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(10, 230, 141, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(10, 530, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.participantLastName = QtWidgets.QLineEdit(self.centralwidget)
        self.participantLastName.setGeometry(QtCore.QRect(320, 180, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.participantLastName.setFont(font)
        self.participantLastName.setText("")
        self.participantLastName.setAlignment(QtCore.Qt.AlignCenter)
        self.participantLastName.setClearButtonEnabled(False)
        self.participantLastName.setObjectName("participantLastName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Add group"))
        self.groupName.setPlaceholderText(_translate("MainWindow", "Group name"))
        self.imageUrl.setPlaceholderText(_translate("MainWindow", "ImageURL"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.addParticipantButton.setText(_translate("MainWindow", "Add participant"))
        self.participantFirstName.setPlaceholderText(_translate("MainWindow", "Participant first name"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.participantLastName.setPlaceholderText(_translate("MainWindow", "Participant last name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
