from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget
from View.GeneratedFiles.UserLoginWithRegisterGenerated import Ui_Form
from PyQt5.QtCore import pyqtSignal
from Controller.MusicSupervisorController import MusicSupervisorController
from Model.Models.MuzickiUrednik import MuzickiUrednik
from View.MusicSupervisorView import MusicSupervisorWindow
from Model.Service.ComplexSerice import ComplexService
from View.RegisteredUserHomeView import RegisteredUserHomeView
from View.RegisterForm import RegisterForm



class LoginFormWithRegister(QWidget,Ui_Form):
    cancel_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_window = None
        self.registered_user_window = None
        self.supervisor_window = None
        self.complex_service = ComplexService()
     
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.return_to_main)
        self.pushButton_3.clicked.connect(self.register)
        
    
    def return_to_main(self):
        self.cancel_signal.emit()
        self.close()
    
    def login(self):
        password = self.lineEdit.text()
        username = self.lineEdit_2.text()
        dto = self.complex_service.account_login(username, password, "Registered user")
        if dto != None:
            self.registered_user_window = RegisteredUserHomeView(dto)
            self.registered_user_window.logout_signal.connect(self.return_to_main)
            self.registered_user_window.show()
            self.close()
        else:
            QMessageBox.information(self, "Poruka", "Incorrect username or password!")

    def register(self):
         self.register_user_window = RegisterForm()
         self.register_user_window.cancel_signal.connect(self.handle_cancel)
         self.register_user_window.show()
         self.close()
         
    def handle_cancel(self):
        self.show()