# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FTN\SIMS\Projekat\SIMSProjekat\UI\AddParticipant.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddParticipant(object):
    def setupUi(self, AddParticipant):
        AddParticipant.setObjectName("AddParticipant")
        AddParticipant.resize(563, 638)
        self.centralwidget = QtWidgets.QWidget(AddParticipant)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(4, 5, 561, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.artname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.artname_edit.setGeometry(QtCore.QRect(10, 80, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.artname_edit.setFont(font)
        self.artname_edit.setText("")
        self.artname_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.artname_edit.setObjectName("artname_edit")
        self.fname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.fname_edit.setGeometry(QtCore.QRect(10, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fname_edit.setFont(font)
        self.fname_edit.setText("")
        self.fname_edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fname_edit.setObjectName("fname_edit")
        self.lname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.lname_edit.setGeometry(QtCore.QRect(310, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lname_edit.setFont(font)
        self.lname_edit.setText("")
        self.lname_edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lname_edit.setObjectName("lname_edit")
        self.gender_label = QtWidgets.QLabel(self.centralwidget)
        self.gender_label.setGeometry(QtCore.QRect(10, 160, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.gender_label.setFont(font)
        self.gender_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.gender_label.setObjectName("gender_label")
        self.birth_label = QtWidgets.QLabel(self.centralwidget)
        self.birth_label.setGeometry(QtCore.QRect(310, 160, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.birth_label.setFont(font)
        self.birth_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.birth_label.setObjectName("birth_label")
        self.genre_label = QtWidgets.QLabel(self.centralwidget)
        self.genre_label.setGeometry(QtCore.QRect(10, 230, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.genre_label.setFont(font)
        self.genre_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.genre_label.setObjectName("genre_label")
        self.datepicker = QtWidgets.QDateEdit(self.centralwidget)
        self.datepicker.setGeometry(QtCore.QRect(310, 200, 241, 31))
        self.datepicker.setObjectName("datepicker")
        self.gender_combo = QtWidgets.QComboBox(self.centralwidget)
        self.gender_combo.setGeometry(QtCore.QRect(10, 200, 241, 31))
        self.gender_combo.setObjectName("gender_combo")
        self.folk_check = QtWidgets.QCheckBox(self.centralwidget)
        self.folk_check.setGeometry(QtCore.QRect(10, 270, 111, 31))
        self.folk_check.setObjectName("folk_check")
        self.pop_check = QtWidgets.QCheckBox(self.centralwidget)
        self.pop_check.setGeometry(QtCore.QRect(120, 270, 111, 31))
        self.pop_check.setObjectName("pop_check")
        self.classic_check = QtWidgets.QCheckBox(self.centralwidget)
        self.classic_check.setGeometry(QtCore.QRect(230, 270, 111, 31))
        self.classic_check.setObjectName("classic_check")
        self.jazz_check = QtWidgets.QCheckBox(self.centralwidget)
        self.jazz_check.setGeometry(QtCore.QRect(340, 270, 111, 31))
        self.jazz_check.setObjectName("jazz_check")
        self.image_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.image_edit.setGeometry(QtCore.QRect(10, 310, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.image_edit.setFont(font)
        self.image_edit.setText("")
        self.image_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.image_edit.setObjectName("image_edit")
        self.biography_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.biography_edit.setGeometry(QtCore.QRect(10, 360, 541, 161))
        self.biography_edit.setObjectName("biography_edit")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(10, 540, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        AddParticipant.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddParticipant)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 26))
        self.menubar.setObjectName("menubar")
        AddParticipant.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddParticipant)
        self.statusbar.setObjectName("statusbar")
        AddParticipant.setStatusBar(self.statusbar)

        self.retranslateUi(AddParticipant)
        QtCore.QMetaObject.connectSlotsByName(AddParticipant)

    def retranslateUi(self, AddParticipant):
        _translate = QtCore.QCoreApplication.translate
        AddParticipant.setWindowTitle(_translate("AddParticipant", "Add participant"))
        self.title_label.setText(_translate("AddParticipant", "Add participant"))
        self.artname_edit.setPlaceholderText(_translate("AddParticipant", "Artistic name"))
        self.fname_edit.setPlaceholderText(_translate("AddParticipant", "Firstname"))
        self.lname_edit.setPlaceholderText(_translate("AddParticipant", "Lastname"))
        self.gender_label.setText(_translate("AddParticipant", "Gender"))
        self.birth_label.setText(_translate("AddParticipant", "Birth date"))
        self.genre_label.setText(_translate("AddParticipant", "Genres"))
        self.folk_check.setText(_translate("AddParticipant", "Folk"))
        self.pop_check.setText(_translate("AddParticipant", "Pop"))
        self.classic_check.setText(_translate("AddParticipant", "Classic"))
        self.jazz_check.setText(_translate("AddParticipant", "Jazz"))
        self.image_edit.setPlaceholderText(_translate("AddParticipant", "Image URL"))
        self.biography_edit.setPlaceholderText(_translate("AddParticipant", "Biography of participant"))
        self.save_button.setText(_translate("AddParticipant", "Save participant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddParticipant = QtWidgets.QMainWindow()
    ui = Ui_AddParticipant()
    ui.setupUi(AddParticipant)
    AddParticipant.show()
    sys.exit(app.exec_())
