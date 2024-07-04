# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FTN\SIMS\Projekat\SIMSProjekat\UI\Participant.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 648)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.banner_widget = QtWidgets.QWidget(self.centralwidget)
        self.banner_widget.setGeometry(QtCore.QRect(0, 0, 1091, 191))
        self.banner_widget.setObjectName("banner_widget")
        self.image_frame = QtWidgets.QFrame(self.banner_widget)
        self.image_frame.setGeometry(QtCore.QRect(40, 20, 211, 211))
        self.image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("image_frame")
        self.artist_label = QtWidgets.QLabel(self.banner_widget)
        self.artist_label.setGeometry(QtCore.QRect(300, -2, 591, 191))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.artist_label.setFont(font)
        self.artist_label.setStyleSheet("color: white")
        self.artist_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.artist_label.setWordWrap(True)
        self.artist_label.setObjectName("artist_label")
        self.genres_label = QtWidgets.QLabel(self.banner_widget)
        self.genres_label.setGeometry(QtCore.QRect(920, 30, 121, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.genres_label.setFont(font)
        self.genres_label.setStyleSheet("color: white")
        self.genres_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.genres_label.setWordWrap(True)
        self.genres_label.setObjectName("genres_label")
        self.artist_label.raise_()
        self.image_frame.raise_()
        self.genres_label.raise_()
        self.stars_label = QtWidgets.QLabel(self.centralwidget)
        self.stars_label.setGeometry(QtCore.QRect(30, 230, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.stars_label.setFont(font)
        self.stars_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stars_label.setObjectName("stars_label")
        self.grade_label = QtWidgets.QLabel(self.centralwidget)
        self.grade_label.setGeometry(QtCore.QRect(30, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.grade_label.setFont(font)
        self.grade_label.setAlignment(QtCore.Qt.AlignCenter)
        self.grade_label.setObjectName("grade_label")
        self.ratings_label = QtWidgets.QLabel(self.centralwidget)
        self.ratings_label.setGeometry(QtCore.QRect(90, 300, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.ratings_label.setFont(font)
        self.ratings_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.ratings_label.setObjectName("ratings_label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(270, 460, 671, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.editor_title_label = QtWidgets.QLabel(self.centralwidget)
        self.editor_title_label.setGeometry(QtCore.QRect(960, 480, 111, 31))
        self.editor_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.editor_title_label.setWordWrap(True)
        self.editor_title_label.setObjectName("editor_title_label")
        self.editor_name_label = QtWidgets.QLabel(self.centralwidget)
        self.editor_name_label.setGeometry(QtCore.QRect(960, 530, 111, 31))
        self.editor_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.editor_name_label.setWordWrap(True)
        self.editor_name_label.setObjectName("editor_name_label")
        self.favourite_button = QtWidgets.QPushButton(self.centralwidget)
        self.favourite_button.setGeometry(QtCore.QRect(30, 350, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.favourite_button.setFont(font)
        self.favourite_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.favourite_button.setAutoExclusive(False)
        self.favourite_button.setObjectName("favourite_button")
        self.favourites_label = QtWidgets.QLabel(self.centralwidget)
        self.favourites_label.setGeometry(QtCore.QRect(90, 360, 151, 31))
        self.favourites_label.setObjectName("favourites_label")
        self.fname_label = QtWidgets.QLabel(self.centralwidget)
        self.fname_label.setGeometry(QtCore.QRect(30, 410, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fname_label.setFont(font)
        self.fname_label.setObjectName("fname_label")
        self.lname_label = QtWidgets.QLabel(self.centralwidget)
        self.lname_label.setGeometry(QtCore.QRect(30, 440, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lname_label.setFont(font)
        self.lname_label.setObjectName("lname_label")
        self.gender_label = QtWidgets.QLabel(self.centralwidget)
        self.gender_label.setGeometry(QtCore.QRect(30, 500, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gender_label.setFont(font)
        self.gender_label.setObjectName("gender_label")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(30, 470, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.biography_label = QtWidgets.QLabel(self.centralwidget)
        self.biography_label.setGeometry(QtCore.QRect(840, 200, 221, 241))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.biography_label.setFont(font)
        self.biography_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.biography_label.setWordWrap(True)
        self.biography_label.setObjectName("biography_label")
        self.pieces_title_label = QtWidgets.QLabel(self.centralwidget)
        self.pieces_title_label.setGeometry(QtCore.QRect(300, 200, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pieces_title_label.setFont(font)
        self.pieces_title_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pieces_title_label.setWordWrap(True)
        self.pieces_title_label.setObjectName("pieces_title_label")
        self.review_button = QtWidgets.QPushButton(self.centralwidget)
        self.review_button.setGeometry(QtCore.QRect(950, 490, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.review_button.setFont(font)
        self.review_button.setObjectName("review_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 26))
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
        self.artist_label.setText(_translate("MainWindow", "Artist Name"))
        self.genres_label.setText(_translate("MainWindow", "Genre1, Genre2, Genre3"))
        self.stars_label.setText(_translate("MainWindow", "🌕🌕🌕🌕🌗"))
        self.grade_label.setText(_translate("MainWindow", "4.5"))
        self.ratings_label.setText(_translate("MainWindow", "from 1234 ratings"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Arial\',\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span></p></body></html>"))
        self.editor_title_label.setText(_translate("MainWindow", "Editor\'s review from:"))
        self.editor_name_label.setText(_translate("MainWindow", "Firstname Lastname"))
        self.favourite_button.setText(_translate("MainWindow", "★"))
        self.favourites_label.setText(_translate("MainWindow", "Add to your favourites"))
        self.fname_label.setText(_translate("MainWindow", "Firstname"))
        self.lname_label.setText(_translate("MainWindow", "Lastname"))
        self.gender_label.setText(_translate("MainWindow", "Gender"))
        self.date_label.setText(_translate("MainWindow", "11.11.2000"))
        self.biography_label.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."))
        self.pieces_title_label.setText(_translate("MainWindow", "Popular musical pieces"))
        self.review_button.setText(_translate("MainWindow", "Add your review"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
