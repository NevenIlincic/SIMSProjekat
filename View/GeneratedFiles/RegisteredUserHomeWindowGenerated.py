# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/RegisteredUserHomeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 1222)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(960, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(20, 10, 881, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 741, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(780, 90, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.search_button.setFont(font)
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_button.setObjectName("search_button")
        self.favourite_label = QtWidgets.QLabel(self.centralwidget)
        self.favourite_label.setGeometry(QtCore.QRect(840, 90, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.favourite_label.setFont(font)
        self.favourite_label.setAlignment(QtCore.Qt.AlignCenter)
        self.favourite_label.setObjectName("favourite_label")
        self.songs_label = QtWidgets.QLabel(self.centralwidget)
        self.songs_label.setGeometry(QtCore.QRect(20, 160, 741, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.songs_label.setFont(font)
        self.songs_label.setObjectName("songs_label")
        self.artists_label = QtWidgets.QLabel(self.centralwidget)
        self.artists_label.setGeometry(QtCore.QRect(20, 340, 741, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.artists_label.setFont(font)
        self.artists_label.setObjectName("artists_label")
        self.albus_label = QtWidgets.QLabel(self.centralwidget)
        self.albus_label.setGeometry(QtCore.QRect(20, 530, 741, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.albus_label.setFont(font)
        self.albus_label.setObjectName("albus_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(830, 140, 20, 571))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 660, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(850, 140, 241, 481))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.artist_layout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.artist_layout_2.setContentsMargins(2, 5, 2, 5)
        self.artist_layout_2.setSpacing(6)
        self.artist_layout_2.setObjectName("artist_layout_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Logout"))
        self.title_label.setText(_translate("MainWindow", "Welcome back, Firstname Lastname!"))
        self.lineEdit.setText(_translate("MainWindow", "Search..."))
        self.search_button.setText(_translate("MainWindow", "🔍"))
        self.favourite_label.setText(_translate("MainWindow", "Your favourites"))
        self.songs_label.setText(_translate("MainWindow", "Songs for you"))
        self.artists_label.setText(_translate("MainWindow", "Suggested artists"))
        self.albus_label.setText(_translate("MainWindow", "Popular albums"))
        self.pushButton_2.setText(_translate("MainWindow", "Make a music list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
